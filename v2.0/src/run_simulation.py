from __future__ import annotations

import csv
import json
import math
import random
from collections import Counter
from pathlib import Path

from model import ACTIONS, ATTENTION_COST_PER_POINT, CHECK_COSTS, LIKELIHOODS, LOSS, LOSS_V1, N_CASES, PRIORS, SEED, STATES, TIME_COST_PER_MINUTE, TRUE_ACTION

ROOT = Path(__file__).resolve().parents[1]


def entropy(p):
    return -sum(v * math.log2(v) for v in p.values() if v > 0)


def normalize(weights):
    total = sum(weights.values())
    return {k: v / total for k, v in weights.items()}


def update(posterior, check, outcome):
    return normalize({s: posterior[s] * LIKELIHOODS[check][s][outcome] for s in STATES})


def action_probs(posterior):
    result = {a: 0.0 for a in ACTIONS}
    for state, probability in posterior.items():
        result[TRUE_ACTION[state]] += probability
    return result


def risks(posterior, loss=LOSS):
    truth = action_probs(posterior)
    return {chosen: sum(truth[actual] * loss[actual][chosen] for actual in ACTIONS) for chosen in ACTIONS}


def best_action(posterior, loss=LOSS):
    values = risks(posterior, loss)
    return min(ACTIONS, key=lambda a: (values[a], ACTIONS.index(a))), values


def generalized_cost(check, multiplier=1.0):
    c = CHECK_COSTS[check]
    return multiplier * (c["money"] + c["minutes"] * TIME_COST_PER_MINUTE + c["attention"] * ATTENTION_COST_PER_POINT)


def outcome_probability(posterior, check, outcome):
    return sum(posterior[s] * LIKELIHOODS[check][s][outcome] for s in STATES)


def expected_after_risk(posterior, check, loss=LOSS):
    total = 0.0
    for outcome in next(iter(LIKELIHOODS[check].values())):
        probability = outcome_probability(posterior, check, outcome)
        if probability:
            total += probability * min(risks(update(posterior, check, outcome), loss).values())
    return total


def expected_information_gain(posterior, check):
    after = 0.0
    for outcome in next(iter(LIKELIHOODS[check].values())):
        probability = outcome_probability(posterior, check, outcome)
        if probability:
            after += probability * entropy(update(posterior, check, outcome))
    return entropy(posterior) - after


def value_of_check(posterior, check, loss=LOSS, evidence_multiplier=1.0):
    current = min(risks(posterior, loss).values())
    return current - expected_after_risk(posterior, check, loss) - generalized_cost(check, evidence_multiplier)


def sample(distribution, rng):
    return rng.choices(list(distribution), weights=list(distribution.values()), k=1)[0]


def generate_cases(n=N_CASES, seed=SEED):
    rng = random.Random(seed)
    cases = []
    for i in range(1, n + 1):
        state = sample(PRIORS, rng)
        evidence = {check: sample(LIKELIHOODS[check][state], rng) for check in LIKELIHOODS}
        cases.append({"case_id": f"W2C{i:03d}", "state": state, "true_action": TRUE_ACTION[state], **evidence})
    return cases


def p0(case):
    prior_actions = action_probs(PRIORS)
    action = max((p, -ACTIONS.index(a), a) for a, p in prior_actions.items())[2]
    return action, [], PRIORS


def p2(case):
    posterior = dict(PRIORS)
    used = []
    for check in LIKELIHOODS:
        posterior = update(posterior, check, case[check])
        used.append(check)
    return best_action(posterior, LOSS_V1)[0], used, posterior


def p3(case, evidence_multiplier=1.0, loss=LOSS_V1, allowed_checks=None):
    posterior = dict(PRIORS)
    unused = list(allowed_checks or LIKELIHOODS)
    used = []
    while unused:
        ranked = sorted(((value_of_check(posterior, c, loss, evidence_multiplier), c) for c in unused), reverse=True)
        value, check = ranked[0]
        if value <= 0:
            break
        posterior = update(posterior, check, case[check])
        used.append(check)
        unused.remove(check)
    return best_action(posterior, loss)[0], used, posterior


def p3b(case):
    # Failure-driven redesign: penalize unnecessary deferral and enforce an
    # entropy budget when information is efficient, avoiding the zero-check trap.
    posterior = dict(PRIORS)
    unused = list(LIKELIHOODS)
    used = []
    while unused and entropy(posterior) > 1.80:
        ranked = sorted(
            ((expected_information_gain(posterior, c) / generalized_cost(c), c) for c in unused),
            reverse=True,
        )
        ratio, check = ranked[0]
        if ratio < 0.50:
            break
        posterior = update(posterior, check, case[check])
        used.append(check)
        unused.remove(check)
    return best_action(posterior, LOSS)[0], used, posterior


def metrics(cases, predictions, loss):
    matrix = {a: {b: 0 for b in ACTIONS} for a in ACTIONS}
    decision_cost = information_cost = checks = human = correct = 0.0
    for case, pred in zip(cases, predictions):
        actual, chosen = case["true_action"], pred["action"]
        matrix[actual][chosen] += 1
        correct += actual == chosen
        decision_cost += loss[actual][chosen]
        information_cost += sum(generalized_cost(c) for c in pred["checks"])
        checks += len(pred["checks"])
        human += chosen == "request human help"
    per_action = {}
    for action in ACTIONS:
        tp = matrix[action][action]
        predicted = sum(matrix[a][action] for a in ACTIONS)
        actual = sum(matrix[action].values())
        per_action[action] = {"precision": tp / predicted if predicted else None, "recall": tp / actual if actual else None}
    n = len(cases)
    return {
        "n": n, "accuracy": correct / n, "per_action": per_action,
        "decision_cost": decision_cost, "information_cost": information_cost,
        "total_cost": decision_cost + information_cost, "average_checks": checks / n,
        "human_review_rate": human / n, "confusion_matrix": matrix,
    }


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)


def main():
    cases = generate_cases()
    policies = {"P0": p0, "P2": p2, "P3": p3, "P3b": p3b}
    all_predictions = {}
    for name, policy in policies.items():
        all_predictions[name] = []
        for case in cases:
            action, checks, posterior = policy(case)
            all_predictions[name].append({"case_id": case["case_id"], "action": action, "checks": checks, "confidence": max(action_probs(posterior).values())})

    write_csv(ROOT / "data" / "simulated-cases.csv", cases, ["case_id", "state", "true_action", *LIKELIHOODS])
    pred_rows = [{**p, "checks": ";".join(p["checks"]), "policy": name} for name, preds in all_predictions.items() for p in preds]
    write_csv(ROOT / "data" / "predictions.csv", pred_rows, ["case_id", "policy", "action", "checks", "confidence"])

    results = {name: metrics(cases, preds, LOSS if name == "P3b" else LOSS_V1) for name, preds in all_predictions.items()}
    (ROOT / "results").mkdir(exist_ok=True)
    (ROOT / "results" / "metrics.json").write_text(json.dumps({"seed": SEED, "n_cases": len(cases), "policies": results}, indent=2) + "\n", encoding="utf-8")

    observed = "ambiguous"
    posterior = update(PRIORS, "E1_fit", observed)
    audit = {
        "prior_sum": sum(PRIORS.values()), "prior_entropy_bits": entropy(PRIORS),
        "update": {"check": "E1_fit", "outcome": observed, "weights": {s: PRIORS[s] * LIKELIHOODS["E1_fit"][s][observed] for s in STATES}, "posterior": posterior},
        "posterior_sum": sum(posterior.values()), "posterior_entropy_bits": entropy(posterior),
        "observed_information_bits": entropy(PRIORS) - entropy(posterior),
        "checks": {c: {"expected_information_gain_bits": expected_information_gain(PRIORS, c), "generalized_cost": generalized_cost(c), "net_value": value_of_check(PRIORS, c), **CHECK_COSTS[c]} for c in LIKELIHOODS},
    }
    (ROOT / "results" / "belief-audit.json").write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({name: {k: v for k, v in result.items() if k in ("accuracy", "decision_cost", "information_cost", "total_cost", "average_checks", "human_review_rate")} for name, result in results.items()}, indent=2))


if __name__ == "__main__":
    main()

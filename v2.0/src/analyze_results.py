from __future__ import annotations

import csv
import json
from pathlib import Path

from model import LOSS, PRIORS
from run_simulation import generate_cases, metrics, p3, p3b

ROOT = Path(__file__).resolve().parents[1]


def evaluate(policy, loss, cases=None):
    cases = cases or generate_cases()
    predictions = []
    for case in cases:
        action, checks, posterior = policy(case)
        predictions.append({"action": action, "checks": checks, "posterior": posterior})
    return metrics(cases, predictions, loss)


def main():
    cases = generate_cases()
    with (ROOT / "data" / "predictions.csv").open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    lookup = {(r["policy"], r["case_id"]): r for r in rows}

    failures = []
    for case in cases:
        p = lookup[("P3b", case["case_id"])]
        if p["action"] != case["true_action"]:
            failures.append({
                "case_id": case["case_id"], "state": case["state"],
                "true_action": case["true_action"], "predicted": p["action"],
                "evidence": {k: case[k] for k in ("E1_fit", "E2_status", "E3_clarify")},
            })
        if len(failures) == 5:
            break

    sensitivity = {
        "false_skip_100x": evaluate(lambda c: p3(c, loss={a: dict(v) for a, v in LOSS.items()}), LOSS),
        "evidence_cost_10x": evaluate(lambda c: p3(c, evidence_multiplier=10.0, loss=LOSS), LOSS),
    }
    # The 100x test requires a separate matrix so the closure and scoring agree.
    extreme = {a: dict(v) for a, v in LOSS.items()}
    for actual in ("apply", "research", "request human help"):
        extreme[actual]["skip"] *= 100
    sensitivity["false_skip_100x"] = evaluate(lambda c: p3(c, loss=extreme), extreme)

    # Prior stress: the world stays fixed, while the policy reasons from a uniform prior.
    import run_simulation as rs
    original = dict(rs.PRIORS)
    uniform = {s: 1 / len(original) for s in original}
    rs.PRIORS.clear(); rs.PRIORS.update(uniform)
    try:
        sensitivity["uniform_unreliable_prior"] = evaluate(p3b, LOSS, cases)
    finally:
        rs.PRIORS.clear(); rs.PRIORS.update(original)

    compact = {}
    for name, result in sensitivity.items():
        compact[name] = {k: result[k] for k in ("accuracy", "decision_cost", "information_cost", "total_cost", "average_checks", "human_review_rate")}
    (ROOT / "results" / "failure-examples.json").write_text(json.dumps(failures, indent=2) + "\n", encoding="utf-8")
    (ROOT / "results" / "sensitivity.json").write_text(json.dumps(compact, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

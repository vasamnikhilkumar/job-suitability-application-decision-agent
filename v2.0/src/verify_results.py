from __future__ import annotations

import csv
import json
import math
from pathlib import Path

from model import LIKELIHOODS, N_CASES, PRIORS, SEED

ROOT = Path(__file__).resolve().parents[1]


def main():
    assert math.isclose(sum(PRIORS.values()), 1.0)
    for check, by_state in LIKELIHOODS.items():
        for state, outcomes in by_state.items():
            assert math.isclose(sum(outcomes.values()), 1.0), (check, state)
    cases = list(csv.DictReader((ROOT / "data" / "simulated-cases.csv").open(encoding="utf-8")))
    predictions = list(csv.DictReader((ROOT / "data" / "predictions.csv").open(encoding="utf-8")))
    metrics = json.loads((ROOT / "results" / "metrics.json").read_text(encoding="utf-8"))
    audit = json.loads((ROOT / "results" / "belief-audit.json").read_text(encoding="utf-8"))
    assert len(cases) == N_CASES == metrics["n_cases"]
    assert metrics["seed"] == SEED
    assert len(predictions) == N_CASES * 4
    assert math.isclose(audit["prior_sum"], 1.0)
    assert math.isclose(audit["posterior_sum"], 1.0)
    assert all(0 <= p["confidence"] if isinstance(p, dict) else True for p in [])
    for result in metrics["policies"].values():
        assert math.isclose(result["total_cost"], result["decision_cost"] + result["information_cost"])
        assert 0 <= result["accuracy"] <= 1
        assert 0 <= result["human_review_rate"] <= 1
    print(f"Verified {N_CASES} identical seeded cases and {len(predictions)} predictions.")


if __name__ == "__main__":
    main()

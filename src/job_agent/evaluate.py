from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ACTIONS = ("apply", "research", "request human help", "skip")
COST = {"research": 3, "request human help": 2}


def load_labels(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    table_labels = {}
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(r"C\d+", cells[0]) and len(cells) >= 5:
            table_labels[cells[0]] = cells[4].strip().lower().replace("**", "")
    if table_labels:
        return table_labels

    headings = list(re.finditer(r"^##\s+(C\d+)\b", text, re.MULTILINE))
    labels = {}
    for i, heading in enumerate(headings):
        body = text[heading.end() : headings[i + 1].start() if i + 1 < len(headings) else len(text)]
        match = re.search(r"Expected (?:correct )?action:\*\*?\s*([^\n]+)|Expected (?:correct )?action:\s*([^\n]+)", body, re.I)
        if not match:
            match = re.search(r"\*\*Expected action:\*\*\s*([^\n]+)", body, re.I)
        if not match:
            raise ValueError(f"No expected action found for {heading.group(1)}")
        labels[heading.group(1)] = next(group for group in match.groups() if group).strip().lower().rstrip(".*")
    return labels


def evaluate(predictions: list[dict], labels: dict[str, str]) -> dict:
    matrix = {expected: {predicted: 0 for predicted in ACTIONS} for expected in ACTIONS}
    costs, correct = 0, 0
    for row in predictions:
        cid, predicted = row["case_id"], row["action"].lower()
        if cid not in labels:
            raise ValueError(f"No label for {cid}")
        expected = labels[cid]
        if predicted not in ACTIONS or expected not in ACTIONS:
            raise ValueError(f"Invalid action in {cid}")
        matrix[expected][predicted] += 1
        correct += predicted == expected
        costs += COST.get(predicted, 0) if predicted == expected else (100 if predicted == "skip" else 5 if predicted == "apply" else COST[predicted])
    total = len(predictions)
    return {"cases": total, "correct": correct, "confusion_matrix": matrix, "total_hypothetical_cost": costs, "mean_hypothetical_cost": costs / total if total else None}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Reveal labels only after predictions have been saved, then score them.")
    p.add_argument("--predictions", type=Path, required=True)
    p.add_argument("--labels", type=Path, default=Path("data/simulated-cases/hidden-labels.md"))
    p.add_argument("--output", type=Path, default=Path("results/simulated-evaluation.json"))
    args = p.parse_args(argv)
    predictions = [json.loads(line) for line in args.predictions.read_text(encoding="utf-8").splitlines() if line.strip()]
    result = evaluate(predictions, load_labels(args.labels))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

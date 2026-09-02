from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from .agent import JobApplicationAgent
from .cases import load_text_cases


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Run agent-visible text cases without loading hidden labels.")
    p.add_argument("--cases", type=Path, default=Path("data/simulated-cases/case-inputs.md"))
    p.add_argument("--output", type=Path, default=Path("results/simulated-predictions.jsonl"))
    p.add_argument("--access-date", type=date.fromisoformat, default=date(2026, 9, 1))
    p.add_argument("--ids", nargs="*", help="Optional case IDs, e.g. C17 C18")
    p.add_argument("--model")
    p.add_argument("--dry-run", action="store_true", help="Validate and list cases without API calls")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        cases = load_text_cases(args.cases)
        if args.ids:
            wanted = set(args.ids)
            cases = [case for case in cases if case.case_id in wanted]
            missing = wanted - {case.case_id for case in cases}
            if missing:
                raise ValueError(f"Unknown case IDs: {', '.join(sorted(missing))}")
        if args.dry_run:
            print(f"Validated {len(cases)} agent-visible cases: {cases[0].case_id}-{cases[-1].case_id}")
            return 0

        completed = _completed_ids(args.output)
        agent = JobApplicationAgent(model=args.model)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("a", encoding="utf-8") as stream:
            for case in cases:
                if case.case_id in completed:
                    print(f"{case.case_id}: already saved; skipped")
                    continue
                decision = agent.analyze_text(case.resume, case.job_post, args.access_date, case.case_id)
                record = {
                    "case_id": case.case_id,
                    "title": case.title,
                    "action": decision.action.value,
                    "policy_reason": decision.policy_reason,
                    "assessment": _assessment_dict(decision.assessment),
                }
                stream.write(json.dumps(record, ensure_ascii=False) + "\n")
                stream.flush()
                print(f"{case.case_id}: {decision.action.value}")
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


def _completed_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {json.loads(line)["case_id"] for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def _assessment_dict(a) -> dict:
    def check(c):
        return {"status": c.status.value, "evidence": list(c.evidence), "explanation": c.explanation, "decision_relevant": c.decision_relevant}
    return {
        "mandatory_requirements": check(a.mandatory_requirements),
        "project_work_evidence": check(a.project_work_evidence),
        "posting_recency": check(a.posting_recency),
        "posting_reliability": check(a.posting_reliability),
        "matched_evidence": list(a.matched_evidence), "partial_evidence": list(a.partial_evidence),
        "mandatory_evidence_not_shown": list(a.mandatory_evidence_not_shown), "uncertainties": list(a.uncertainties),
        "research_question": a.research_question, "action_changing_answer": a.action_changing_answer,
        "human_judgment_question": a.human_judgment_question, "conclusive_hard_stop": a.conclusive_hard_stop,
        "hard_stop_reason": a.hard_stop_reason,
    }

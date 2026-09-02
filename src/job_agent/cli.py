from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

from .agent import JobApplicationAgent
from .render import render


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Recommend the next action for one resume and one job post.")
    p.add_argument("--resume", required=True, type=Path, help="Resume image, PDF, or text file")
    p.add_argument("--job-url", required=True, help="Exact job-post URL")
    p.add_argument("--access-date", type=date.fromisoformat, default=date.today(), help="YYYY-MM-DD (default: today)")
    p.add_argument("--job-text", type=Path, help="Optional saved job-page text; improves reproducibility")
    p.add_argument("--model", help="OpenAI model ID (default: JOB_AGENT_MODEL or gpt-5.4)")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if not args.resume.is_file():
            raise FileNotFoundError(f"Resume not found: {args.resume}")
        if args.job_text and not args.job_text.is_file():
            raise FileNotFoundError(f"Job-page snapshot not found: {args.job_text}")
        snapshot = args.job_text.read_text(encoding="utf-8") if args.job_text else None
        result = JobApplicationAgent(model=args.model).analyze(args.resume, args.job_url, args.access_date, snapshot)
        print(render(result))
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

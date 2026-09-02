from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TextCase:
    case_id: str
    title: str
    resume: str
    job_post: str


CASE_HEADING = re.compile(r"^##\s+(C\d+)\s+[—-]\s+(.+?)\s*$", re.MULTILINE)


def load_text_cases(path: str | Path) -> list[TextCase]:
    text = Path(path).read_text(encoding="utf-8")
    matches = list(CASE_HEADING.finditer(text))
    cases: list[TextCase] = []
    for index, match in enumerate(matches):
        body = text[match.end() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        resume = _field(body, "Résumé") or _field(body, "Resume")
        job = _field(body, "Job post")
        if not resume or not job:
            raise ValueError(f"{match.group(1)} must contain Résumé and Job post fields")
        cases.append(TextCase(match.group(1), match.group(2).strip(), resume, job))
    if not cases:
        raise ValueError(f"No Cxx cases found in {path}")
    ids = [case.case_id for case in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate case IDs found")
    return cases


def _field(body: str, name: str) -> str:
    match = re.search(rf"\*\*{re.escape(name)}:\*\*\s*(.+?)(?=\n\s*\n|\n\*\*|\Z)", body, re.DOTALL)
    return " ".join(match.group(1).split()) if match else ""


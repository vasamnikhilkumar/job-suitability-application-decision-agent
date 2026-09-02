from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class CheckStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    UNCLEAR = "unclear"


class Action(str, Enum):
    APPLY = "apply"
    RESEARCH = "research"
    HUMAN_HELP = "request human help"
    SKIP = "skip"


@dataclass(frozen=True)
class Check:
    status: CheckStatus
    evidence: tuple[str, ...] = ()
    explanation: str = ""
    decision_relevant: bool = True

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Check":
        return cls(
            status=CheckStatus(value["status"].lower()),
            evidence=tuple(value.get("evidence", [])),
            explanation=value.get("explanation", ""),
            decision_relevant=bool(value.get("decision_relevant", True)),
        )


@dataclass(frozen=True)
class Assessment:
    mandatory_requirements: Check
    project_work_evidence: Check
    posting_recency: Check
    posting_reliability: Check
    matched_evidence: tuple[str, ...] = ()
    partial_evidence: tuple[str, ...] = ()
    mandatory_evidence_not_shown: tuple[str, ...] = ()
    uncertainties: tuple[str, ...] = ()
    research_question: str = ""
    action_changing_answer: str = ""
    human_judgment_question: str = ""
    conclusive_hard_stop: bool = False
    hard_stop_reason: str = ""

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Assessment":
        return cls(
            mandatory_requirements=Check.from_dict(value["mandatory_requirements"]),
            project_work_evidence=Check.from_dict(value["project_work_evidence"]),
            posting_recency=Check.from_dict(value["posting_recency"]),
            posting_reliability=Check.from_dict(value["posting_reliability"]),
            matched_evidence=tuple(value.get("matched_evidence", [])),
            partial_evidence=tuple(value.get("partial_evidence", [])),
            mandatory_evidence_not_shown=tuple(value.get("mandatory_evidence_not_shown", [])),
            uncertainties=tuple(value.get("uncertainties", [])),
            research_question=value.get("research_question", ""),
            action_changing_answer=value.get("action_changing_answer", ""),
            human_judgment_question=value.get("human_judgment_question", ""),
            conclusive_hard_stop=bool(value.get("conclusive_hard_stop", False)),
            hard_stop_reason=value.get("hard_stop_reason", ""),
        )


@dataclass(frozen=True)
class Decision:
    action: Action
    assessment: Assessment
    policy_reason: str
    warnings: tuple[str, ...] = field(default_factory=tuple)


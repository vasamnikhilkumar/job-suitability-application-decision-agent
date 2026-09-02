from __future__ import annotations

from .models import Decision


def _items(values: tuple[str, ...]) -> str:
    return "; ".join(values) if values else "None shown"


def render(decision: Decision) -> str:
    a = decision.assessment
    checks = (
        f"mandatory requirements={a.mandatory_requirements.status.value}; "
        f"project/work evidence={a.project_work_evidence.status.value}; "
        f"posting recency={a.posting_recency.status.value}; "
        f"posting reliability={a.posting_reliability.status.value}"
    )
    question = a.research_question if decision.action.value == "research" else "Not applicable"
    reconsider = a.action_changing_answer or a.human_judgment_question or "Reconsider if material evidence changes."
    return "\n".join([
        f"Action: {decision.action.value}",
        f"Check results: {checks}",
        f"Matched evidence: {_items(a.matched_evidence)}",
        f"Partial evidence: {_items(a.partial_evidence)}",
        f"Mandatory evidence not shown: {_items(a.mandatory_evidence_not_shown)}",
        f"Uncertainty: {_items(a.uncertainties)}",
        f"Research question, if applicable: {question}",
        f"Condition under which the candidate should reconsider the decision: {reconsider}",
    ])


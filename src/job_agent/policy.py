from __future__ import annotations

from .models import Action, Assessment, CheckStatus, Decision


def decide(assessment: Assessment) -> Decision:
    """Apply the frozen Version 1 rules in their documented order."""
    checks = (
        assessment.mandatory_requirements,
        assessment.project_work_evidence,
        assessment.posting_recency,
        assessment.posting_reliability,
    )

    if assessment.conclusive_hard_stop:
        return Decision(Action.SKIP, assessment, assessment.hard_stop_reason or "Conclusive mandatory failure")

    unclear = [c for c in checks if c.status is CheckStatus.UNCLEAR and c.decision_relevant]
    if unclear:
        if assessment.human_judgment_question and not assessment.research_question:
            return Decision(Action.HUMAN_HELP, assessment, "The unresolved issue requires a judgment call")
        return Decision(Action.RESEARCH, assessment, "A decision-relevant factual check is unclear")

    if all(c.status is CheckStatus.PASS for c in checks):
        return Decision(Action.APPLY, assessment, "All four evidence checks pass")

    mandatory = assessment.mandatory_requirements.status
    evidence = assessment.project_work_evidence.status
    reliability = assessment.posting_reliability.status

    if mandatory is CheckStatus.FAIL and evidence is CheckStatus.FAIL:
        return Decision(Action.SKIP, assessment, "Mandatory and role-specific evidence checks both fail")

    if assessment.human_judgment_question:
        return Decision(Action.HUMAN_HELP, assessment, "The remaining issue is transferability, equivalence, or preference")

    core_passes = sum(s is CheckStatus.PASS for s in (mandatory, evidence))
    if reliability is CheckStatus.FAIL and core_passes == 1:
        return Decision(Action.HUMAN_HELP, assessment, "Posting reliability fails and exactly one candidate-fit check passes")

    failures = sum(c.status is CheckStatus.FAIL for c in checks)
    if failures == 1 and assessment.research_question:
        return Decision(Action.RESEARCH, assessment, "One failed check may be changed by a factual answer")

    return Decision(Action.HUMAN_HELP, assessment, "No deterministic rule safely resolves the case")


from job_agent.models import Assessment, Check, CheckStatus, Action
from job_agent.policy import decide


def assessment(m="pass", e="pass", r="pass", reliability="pass", **kwargs):
    return Assessment(
        mandatory_requirements=Check(CheckStatus(m)),
        project_work_evidence=Check(CheckStatus(e)),
        posting_recency=Check(CheckStatus(r)),
        posting_reliability=Check(CheckStatus(reliability)),
        **kwargs,
    )


def test_apply_requires_all_checks_to_pass():
    assert decide(assessment()).action is Action.APPLY


def test_hard_stop_precedes_uncertainty():
    value = assessment(m="fail", r="unclear", conclusive_hard_stop=True, hard_stop_reason="License required")
    assert decide(value).action is Action.SKIP


def test_decision_relevant_unknown_causes_research():
    value = assessment(m="unclear", research_question="Does the candidate have work authorization?")
    assert decide(value).action is Action.RESEARCH


def test_irrelevant_unknown_does_not_force_research():
    value = Assessment(
        Check(CheckStatus.PASS), Check(CheckStatus.PASS),
        Check(CheckStatus.UNCLEAR, decision_relevant=False), Check(CheckStatus.PASS)
    )
    assert decide(value).action is Action.HUMAN_HELP


def test_both_fit_checks_fail_means_skip():
    assert decide(assessment(m="fail", e="fail", reliability="fail")).action is Action.SKIP


def test_judgment_call_goes_to_human():
    value = assessment(m="unclear", human_judgment_question="Is adjacent experience transferable?")
    assert decide(value).action is Action.HUMAN_HELP


def test_single_resolvable_failure_causes_research():
    value = assessment(r="fail", research_question="Is this exact vacancy still progressing applicants?")
    assert decide(value).action is Action.RESEARCH

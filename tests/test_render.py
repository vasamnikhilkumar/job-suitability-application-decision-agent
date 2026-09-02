from job_agent.models import Assessment, Check, CheckStatus
from job_agent.policy import decide
from job_agent.render import render


def test_render_has_exact_required_sections():
    passed = Check(CheckStatus.PASS, ("source: evidence",), "shown")
    output = render(decide(Assessment(
        mandatory_requirements=passed,
        project_work_evidence=passed,
        posting_recency=passed,
        posting_reliability=passed,
        matched_evidence=("resume: Python",),
    )))

    expected_prefixes = [
        "Action:",
        "Check results:",
        "Matched evidence:",
        "Partial evidence:",
        "Mandatory evidence not shown:",
        "Uncertainty:",
        "Research question, if applicable:",
        "Condition under which the candidate should reconsider the decision:",
    ]
    lines = output.splitlines()
    assert len(lines) == 8
    assert all(line.startswith(prefix) for line, prefix in zip(lines, expected_prefixes))


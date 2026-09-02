from job_agent.cases import load_text_cases


def test_repository_simulated_cases_are_complete_and_agent_visible_only():
    cases = load_text_cases("data/simulated-cases/case-inputs.md")
    assert [case.case_id for case in cases] == [f"C{i}" for i in range(17, 51)]
    assert all(case.resume and case.job_post for case in cases)
    assert "Expected action" not in " ".join(case.resume + case.job_post for case in cases)


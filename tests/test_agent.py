import json
from datetime import date
from types import SimpleNamespace

from job_agent.agent import JobApplicationAgent
from job_agent.models import Action


class FakeResponses:
    def __init__(self):
        self.request = None

    def create(self, **kwargs):
        self.request = kwargs
        check = {"status": "pass", "evidence": ["source: evidence"], "explanation": "shown", "decision_relevant": True}
        payload = {
            "mandatory_requirements": check,
            "project_work_evidence": check,
            "posting_recency": check,
            "posting_reliability": check,
            "matched_evidence": ["resume: evidence"],
            "partial_evidence": [],
            "mandatory_evidence_not_shown": [],
            "uncertainties": [],
            "research_question": "",
            "action_changing_answer": "",
            "human_judgment_question": "",
            "conclusive_hard_stop": False,
            "hard_stop_reason": "",
        }
        return SimpleNamespace(output_text=json.dumps(payload))


def test_agent_uses_structured_extraction_then_local_policy(tmp_path):
    resume = tmp_path / "resume.txt"
    resume.write_text("Python developer", encoding="utf-8")
    responses = FakeResponses()
    client = SimpleNamespace(responses=responses)

    decision = JobApplicationAgent(client=client).analyze(
        resume, "https://example.com/job", date(2026, 9, 1), "Job snapshot"
    )

    assert decision.action is Action.APPLY
    assert responses.request["store"] is False
    assert responses.request["text"]["format"]["type"] == "json_schema"
    assert "tools" not in responses.request


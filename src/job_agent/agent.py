from __future__ import annotations

import base64
import json
import mimetypes
import os
from datetime import date
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

from .models import Assessment, Decision
from .policy import decide
from .prompt import ASSESSMENT_SCHEMA, SYSTEM_PROMPT


class JobApplicationAgent:
    def __init__(self, model: str | None = None, client=None) -> None:
        if client is None:
            # A process-level environment variable takes precedence over the local file.
            load_dotenv(find_dotenv(usecwd=True), override=False)
            try:
                from openai import OpenAI
            except ImportError as exc:
                raise RuntimeError("Install the project first: pip install -e .") from exc
            client = OpenAI()
        self.client = client
        self.model = model or os.getenv("JOB_AGENT_MODEL", "gpt-5.4")

    def analyze(
        self,
        resume: str | Path,
        job_url: str,
        access_date: date,
        job_text: str | None = None,
    ) -> Decision:
        path = Path(resume)
        if not path.is_file():
            raise FileNotFoundError(f"Resume not found: {path}")
        if not job_url.startswith(("https://", "http://")):
            raise ValueError("job_url must be an http(s) URL")

        content = [
            {
                "type": "input_text",
                "text": (
                    f"Access date: {access_date.isoformat()}\nExact job URL: {job_url}\n"
                    + (f"Job-page snapshot supplied by user:\n{job_text}" if job_text else
                       "No page snapshot was supplied. Use web search to inspect the exact URL and state when it cannot be accessed.")
                ),
            },
            self._resume_content(path),
        ]
        return self._request(content, use_web_search=job_text is None)

    def analyze_text(self, resume_text: str, job_text: str, access_date: date, source: str = "supplied case") -> Decision:
        """Analyze an entirely text-based case without any live-page retrieval."""
        if not resume_text.strip() or not job_text.strip():
            raise ValueError("Both resume_text and job_text are required")
        content = [{
            "type": "input_text",
            "text": (
                f"Access date: {access_date.isoformat()}\nSource: {source}\n"
                f"Resume evidence:\n{resume_text}\n\nJob-post evidence:\n{job_text}"
            ),
        }]
        return self._request(content, use_web_search=False)

    def _request(self, content: list[dict[str, str]], use_web_search: bool) -> Decision:
        kwargs = {
            "model": self.model,
            "instructions": SYSTEM_PROMPT,
            "input": [{"role": "user", "content": content}],
            "text": {"format": {"type": "json_schema", "name": "job_assessment", "strict": True, "schema": ASSESSMENT_SCHEMA}},
            "store": False,
        }
        if use_web_search:
            kwargs["tools"] = [{"type": "web_search"}]

        response = self.client.responses.create(**kwargs)
        if not getattr(response, "output_text", None):
            raise RuntimeError("The model returned no assessment text")
        assessment = Assessment.from_dict(json.loads(response.output_text))
        return decide(assessment)

    @staticmethod
    def _resume_content(path: Path) -> dict[str, str]:
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        data_url = f"data:{mime};base64,{encoded}"
        if mime.startswith("image/"):
            return {"type": "input_image", "image_url": data_url, "detail": "high"}
        if mime == "application/pdf":
            return {"type": "input_file", "filename": path.name, "file_data": data_url}
        if mime.startswith("text/"):
            return {"type": "input_text", "text": "Resume:\n" + path.read_text(encoding="utf-8")}
        raise ValueError("Resume must be an image, PDF, or UTF-8 text file")

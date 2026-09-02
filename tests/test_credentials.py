import os

import pytest
from dotenv import dotenv_values

from job_agent.credentials import save_api_key


def test_save_api_key_to_local_env(tmp_path):
    target = save_api_key("sk-test-value", tmp_path / ".env")
    assert dotenv_values(target)["OPENAI_API_KEY"] == "sk-test-value"


def test_rejects_empty_or_non_key_values(tmp_path):
    with pytest.raises(ValueError):
        save_api_key("", tmp_path / ".env")
    with pytest.raises(ValueError):
        save_api_key("not-a-key", tmp_path / ".env")


from __future__ import annotations

import getpass
import os
from pathlib import Path

from dotenv import set_key


def save_api_key(key: str, destination: Path | None = None) -> Path:
    """Save a key to a git-ignored local dotenv file without logging it."""
    value = key.strip()
    if not value:
        raise ValueError("API key cannot be empty")
    if not value.startswith("sk-"):
        raise ValueError("This does not look like an OpenAI API key (expected an sk- prefix)")
    target = destination or Path.cwd() / ".env"
    set_key(str(target), "OPENAI_API_KEY", value, quote_mode="always")
    return target


def main() -> int:
    if os.getenv("OPENAI_API_KEY"):
        answer = input("OPENAI_API_KEY is already set in this terminal. Replace the project-local key? [y/N] ")
        if answer.strip().lower() not in {"y", "yes"}:
            print("No changes made.")
            return 0
    key = getpass.getpass("Paste your OpenAI API key (input is hidden): ")
    try:
        target = save_api_key(key)
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1
    print(f"Key saved locally in {target.name}. Future job-agent runs will load it automatically.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


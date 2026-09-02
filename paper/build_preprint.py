"""Compile the IJCAI-style course preprint with Tectonic."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
OUTPUT = ROOT / "output" / "pdf"
FINAL = OUTPUT / "job-application-agent-course-preprint.pdf"


def find_tectonic() -> str:
    configured = os.getenv("TECTONIC")
    local = ROOT / "tmp" / "pdfs" / "tectonic" / "bin" / "tectonic.exe"
    executable = configured or shutil.which("tectonic") or (str(local) if local.exists() else None)
    if not executable:
        raise SystemExit("Tectonic was not found. Install it or set the TECTONIC environment variable.")
    return executable


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [find_tectonic(), "-X", "compile", "main.tex", "--outdir", str(OUTPUT), "--keep-logs"],
        cwd=PAPER,
        check=True,
    )
    generated = OUTPUT / "main.pdf"
    if not generated.exists():
        raise SystemExit("Compilation completed without producing main.pdf")
    shutil.copy2(generated, FINAL)
    shutil.copy2(generated, PAPER / "preprint.pdf")
    print(FINAL)


if __name__ == "__main__":
    main()

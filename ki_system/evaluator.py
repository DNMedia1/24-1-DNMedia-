"""Evaluate generated code via simple checks."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys


@dataclass
class EvaluationResult:
    success: bool
    output: str


def run_py_compile(path: Path) -> EvaluationResult:
    try:
        subprocess.check_output([sys.executable, "-m", "py_compile", str(path)])
        return EvaluationResult(True, "Syntax OK")
    except subprocess.CalledProcessError as exc:
        return EvaluationResult(False, exc.output.decode())

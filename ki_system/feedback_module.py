"""Feedback utilities for generated code."""
from __future__ import annotations
from pathlib import Path
from .evaluator import run_py_compile, EvaluationResult


def provide_feedback(code_path: Path) -> EvaluationResult:
    result = run_py_compile(code_path)
    return result

"""Feedback utilities for generated code."""
from __future__ import annotations
from pathlib import Path
from .evaluator import run_py_compile, EvaluationResult
import logging


log = logging.getLogger(__name__)


def provide_feedback(code_path: Path) -> EvaluationResult:
    log.debug("Providing feedback for %s", code_path)
    result = run_py_compile(code_path)
    return result

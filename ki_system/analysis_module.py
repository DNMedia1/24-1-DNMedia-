"""Simple analysis utilities for task descriptions."""
from dataclasses import dataclass
from typing import Optional
import re


@dataclass
class TaskAnalysis:
    language: str
    complexity: str


def detect_language(task: str) -> str:
    task_lower = task.lower()
    if "python" in task_lower:
        return "python"
    if "javascript" in task_lower or "js" in task_lower:
        return "javascript"
    if "c#" in task_lower:
        return "csharp"
    return "plain"


def estimate_complexity(task: str) -> str:
    word_count = len(re.findall(r"\w+", task))
    if word_count < 20:
        return "low"
    if word_count < 50:
        return "medium"
    return "high"


def analyze_task(task: str) -> TaskAnalysis:
    return TaskAnalysis(language=detect_language(task), complexity=estimate_complexity(task))

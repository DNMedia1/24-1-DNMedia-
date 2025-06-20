"""Input module for the autonomous code generation system."""
from pathlib import Path
from typing import Optional


def read_task_from_file(path: Path) -> str:
    """Read a task description from a text file."""
    return path.read_text(encoding="utf-8")


def get_task(task: Optional[str] = None, file: Optional[Path] = None) -> str:
    """Return the task description from CLI input or file."""
    if task:
        return task
    if file and file.exists():
        return read_task_from_file(file)
    raise ValueError("No task provided")

"""Input module for the autonomous code generation system."""
from pathlib import Path
from typing import Optional
import logging


log = logging.getLogger(__name__)


def read_task_from_file(path: Path) -> str:
    """Read a task description from a text file."""
    log.debug("Reading task from %s", path)
    return path.read_text(encoding="utf-8")


def get_task(task: Optional[str] = None, file: Optional[Path] = None) -> str:
    """Return the task description from CLI input or file."""
    if task:
        log.debug("Using task from CLI")
        return task
    if file and file.exists():
        log.debug("Using task from file")
        return read_task_from_file(file)
    raise ValueError("No task provided")

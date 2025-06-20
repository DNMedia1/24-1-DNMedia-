"""Command-line interface for the autonomous code generator."""
from __future__ import annotations
import argparse
from pathlib import Path
import logging

from .input_module import get_task
from .analysis_module import analyze_task
from .code_generator import CodeGenerator, GenerationConfig
from .feedback_module import provide_feedback


log = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser(description="Autonomous code generator")
    parser.add_argument("--log-level", default="INFO", help="Logging level")
    parser.add_argument("--task", help="Task description text")
    parser.add_argument("--file", type=Path, help="Path to a text file with the task")
    parser.add_argument(
        "--output", type=Path, default=Path("generated_code.py"), help="Output file"
    )
    parser.add_argument(
        "--model", default="bigcode/starcoderbase", help="Hugging Face model name"
    )
    args = parser.parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level.upper(), logging.INFO))

    task = get_task(task=args.task, file=args.file)
    analysis = analyze_task(task)
    log.info("Detected language: %s complexity: %s", analysis.language, analysis.complexity)

    generator = CodeGenerator(GenerationConfig(model_name=args.model))
    path = generator.generate_to_file(task, args.output)
    result = provide_feedback(path)
    if result.success:
        log.info("Code generated successfully: %s", path)
    else:
        log.error("Code generation failed: %s", result.output)


if __name__ == "__main__":
    main()

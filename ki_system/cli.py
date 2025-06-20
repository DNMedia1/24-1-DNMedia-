"""Command-line interface for the autonomous code generator."""
from __future__ import annotations
import argparse
from pathlib import Path

from .input_module import get_task
from .analysis_module import analyze_task
from .code_generator import CodeGenerator, GenerationConfig
from .feedback_module import provide_feedback


def main() -> None:
    parser = argparse.ArgumentParser(description="Autonomous code generator")
    parser.add_argument("--task", help="Task description text")
    parser.add_argument("--file", type=Path, help="Path to a text file with the task")
    parser.add_argument(
        "--output", type=Path, default=Path("generated_code.py"), help="Output file"
    )
    parser.add_argument(
        "--model", default="bigcode/starcoderbase", help="Hugging Face model name"
    )
    args = parser.parse_args()

    task = get_task(task=args.task, file=args.file)
    analysis = analyze_task(task)
    print(f"Detected language: {analysis.language}, complexity: {analysis.complexity}")

    generator = CodeGenerator(GenerationConfig(model_name=args.model))
    path = generator.generate_to_file(task, args.output)
    result = provide_feedback(path)
    if result.success:
        print(f"Code generated successfully: {path}")
    else:
        print(f"Code generation failed: {result.output}")


if __name__ == "__main__":
    main()

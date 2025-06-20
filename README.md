# 24-1-DNMedia-

This repository now contains a basic autonomous code generation system built in Python. The system uses open-source models from Hugging Face to generate code for development tasks.

## Setup

1. Install Python 3.10 or newer.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the CLI with a task description:
   ```bash
   python -m ki_system.cli --task "Write a Python function to validate email addresses"
   ```
   The generated code will be written to `generated_code.py`.

## Modules

- **input_module.py** – reads tasks from CLI or text files.
- **analysis_module.py** – determines target language and complexity.
- **code_generator.py** – loads a Hugging Face model (e.g. `bigcode/starcoderbase`) and produces code.
- **evaluator.py** – performs simple syntax checks.
- **feedback_module.py** – provides feedback based on evaluation results.
- **cli.py** – command line entry point.

This structure offers a starting point for autonomous code generation workflows.

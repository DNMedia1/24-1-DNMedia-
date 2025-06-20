# 24-1-DNMedia-

This repository now contains a basic autonomous code generation system built in Python. It uses open-source models from Hugging Face to generate code for development tasks, including Business Central AL snippets.

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
   Use `--log-level DEBUG` for verbose logging.

4. Example for generating an AL test stub:
   ```bash
   python -m ki_system.cli --task "Erstelle einen Business Central AL Test fuer eine Verkaufsbelegprüfung"
   ```

## Modules

- **input_module.py** – reads tasks from CLI or text files.
- **analysis_module.py** – determines target language (Python, JS, C#, AL) and complexity.
- **code_generator.py** – loads a Hugging Face model (e.g. `bigcode/starcoderbase`) and produces code.
- **evaluator.py** – performs simple syntax checks.
- **feedback_module.py** – provides feedback based on evaluation results.
- **cli.py** – command line entry point.

This structure offers a starting point for autonomous code generation workflows.

## Docker Usage

A Dockerfile and optional `docker-compose.yml` are provided for running the code generator in an isolated container.

### Build the image
```bash
docker build -t ki-system .
```

### Run with volumes
```bash
docker run --rm \
  -v $(pwd)/input:/input \
  -v $(pwd)/output:/output \
  -v $(pwd)/logs:/logs \
  -v $(pwd)/models:/models \
  ki-system --task "Write a Python function to validate email addresses" --output /output/generated_code.py
```

Volumes allow you to supply tasks and store generated code and logs outside the container. Set `TRANSFORMERS_OFFLINE=1` to load models from `/models` without internet access.

### Using docker-compose with GPU
If you have the NVIDIA Container Toolkit installed, start the service with GPU support:
```bash
docker compose run ki-system --task "Write a Python function to validate email addresses" --output /output/generated_code.py
```
This uses the compose file's `runtime: nvidia` configuration.

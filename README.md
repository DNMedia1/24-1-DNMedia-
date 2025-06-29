# 24-1-DNMedia-

This repository now contains a basic autonomous code generation system built in Python. The system uses open-source models from Hugging Face to generate code for development tasks.

---

## Deutsch

Dieses Repository enthält ein grundlegendes autonomes Code-Generierungssystem in Python. Das System nutzt Open-Source-Modelle von Hugging Face, um Code für Entwicklungsaufgaben zu erzeugen.

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

### Deutsche Anleitung

1. Python 3.10 oder neuer installieren.
2. Abh\u00e4ngigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```
3. Die CLI mit einer Aufgabenbeschreibung ausf\u00fchren:
   ```bash
   python -m ki_system.cli --task "Write a Python function to validate email addresses"
   ```
   Der generierte Code wird in `generated_code.py` gespeichert.

## Modules

- **input_module.py** – reads tasks from CLI or text files.
- **analysis_module.py** – determines target language and complexity.
- **code_generator.py** – loads a Hugging Face model (e.g. `bigcode/starcoderbase`) and produces code.
- **evaluator.py** – performs simple syntax checks.
- **feedback_module.py** – provides feedback based on evaluation results.
- **cli.py** – command line entry point.

### Module auf Deutsch

- **input_module.py** – liest Aufgaben von der Kommandozeile oder aus Textdateien.
- **analysis_module.py** – bestimmt Zielsprache und Komplexität.
- **code_generator.py** – lädt ein Hugging-Face-Modell (z. B. `bigcode/starcoderbase`) und erzeugt Code.
- **evaluator.py** – führt einfache Syntaxprüfungen durch.
- **feedback_module.py** – gibt Rückmeldungen basierend auf den Ergebnissen aus.
- **cli.py** – Kommandozeileneinstiegspunkt.

This structure offers a starting point for autonomous code generation workflows.

Diese Struktur bietet einen Ausgangspunkt für autonome Code-Generierungsabläufe.

---

## Stock Analysis Tool

The repository also contains an initial folder structure for a stock market analysis and forecasting project. The main components are located in `stock_analysis/`:

- `data/` – placeholder for imported market data
- `models/` – machine learning models
- `src/` – Python source code
- `tests/` – unit tests
- `docs/` – project documentation

### Aktienanalyse-Werkzeug (Deutsch)

Dieses Repository enthält zudem eine erste Ordnerstruktur für ein Projekt zur Analyse und Prognose von Börsendaten. Die wichtigsten Komponenten befinden sich in `stock_analysis/`:

- `data/` – Ablage für importierte Marktdaten
- `models/` – Machine-Learning-Modelle
- `src/` – Python-Quellcode
- `tests/` – Unit-Tests
- `docs/` – Projektdokumentation

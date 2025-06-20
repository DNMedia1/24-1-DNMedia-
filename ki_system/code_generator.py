"""Code generation utilities using Hugging Face models."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from pathlib import Path
import logging

try:
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
except ModuleNotFoundError as exc:  # pragma: no cover - handled at runtime
    AutoTokenizer = AutoModelForCausalLM = pipeline = None  # type: ignore


log = logging.getLogger(__name__)


@dataclass
class GenerationConfig:
    model_name: str = "bigcode/starcoderbase"  # open-source model
    max_new_tokens: int = 128
    temperature: float = 0.2


class CodeGenerator:
    def __init__(self, config: GenerationConfig):
        self.config = config
        if pipeline is None:
            raise RuntimeError(
                "transformers package is required for code generation."
            )
        log.debug("Loading model %s", config.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(config.model_name)
        self.generator = pipeline(
            "text-generation", model=self.model, tokenizer=self.tokenizer
        )

    def generate_code(self, prompt: str) -> str:
        log.debug("Generating code for prompt of length %d", len(prompt))
        result = self.generator(
            prompt,
            max_new_tokens=self.config.max_new_tokens,
            temperature=self.config.temperature,
            do_sample=True,
        )[0]["generated_text"]
        return result[len(prompt) :]

    def generate_to_file(self, prompt: str, path: Path) -> Path:
        code = self.generate_code(prompt)
        path.write_text(code, encoding="utf-8")
        log.info("Generated code written to %s", path)
        return path

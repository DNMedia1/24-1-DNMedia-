"""Code generation utilities using Hugging Face models."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from pathlib import Path


@dataclass
class GenerationConfig:
    model_name: str = "bigcode/starcoderbase"  # open-source model
    max_new_tokens: int = 128
    temperature: float = 0.2


class CodeGenerator:
    def __init__(self, config: GenerationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(config.model_name)
        self.generator = pipeline(
            "text-generation", model=self.model, tokenizer=self.tokenizer
        )

    def generate_code(self, prompt: str) -> str:
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
        return path

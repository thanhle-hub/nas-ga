"""
Ollama client.
"""

from __future__ import annotations

from .base import BaseLLM
from .response import LLMResponse
from .config import LLMConfig


class OllamaClient(BaseLLM):

    def __init__(
        self,
        config: LLMConfig,
    ) -> None:

        self.config = config


    def generate(
        self,
        prompt: str,
    ) -> LLMResponse:

        return LLMResponse(

            text=f"[Ollama Stub] {prompt}",

            model=self.config.model,

        )
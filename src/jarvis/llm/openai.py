"""
OpenAI client.
"""

from __future__ import annotations

from .base import BaseLLM
from .response import LLMResponse
from .config import LLMConfig


class OpenAIClient(BaseLLM):

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

            text=f"[OpenAI Stub] {prompt}",

            model=self.config.model,

        )
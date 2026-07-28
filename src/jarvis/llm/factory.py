"""
LLM factory.
"""

from __future__ import annotations

from .mock import MockLLM
from .openai import OpenAIClient
from .ollama import OllamaClient
from .config import LLMConfig


class LLMFactory:

    @staticmethod
    def create(
        config: LLMConfig,
    ):

        provider = config.provider.lower()

        if provider == "mock":

            return MockLLM()

        if provider == "openai":

            return OpenAIClient(config)

        if provider == "ollama":

            return OllamaClient(config)

        raise ValueError(
            f"Unknown LLM provider: {provider}"
        )
"""
LLM configuration.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LLMConfig:

    provider: str = "mock"

    model: str = ""

    api_key: str = ""

    base_url: str = ""

    temperature: float = 0.0

    max_tokens: int = 1024
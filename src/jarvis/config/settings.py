"""
Global application settings.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Settings:
    """Application configuration."""

    app_name: str = "JARVIS OS"
    version: str = "0.1.0"

    @property
    def project_root(self) -> Path:
        return Path(__file__).resolve().parents[3]

    @property
    def log_directory(self) -> Path:
        return self.project_root / "logs"

    @property
    def data_directory(self) -> Path:
        return self.project_root / "data"
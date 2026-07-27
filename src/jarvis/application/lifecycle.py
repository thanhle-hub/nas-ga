"""
Application lifecycle management.
"""

from __future__ import annotations

import logging


class ApplicationLifecycle:
    """Controls startup and shutdown."""

    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    def startup(self) -> None:
        self._logger.info("Starting JARVIS...")

    def shutdown(self) -> None:
        self._logger.info("Stopping JARVIS...")
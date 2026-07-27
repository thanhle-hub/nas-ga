"""
Application runtime.
"""

from __future__ import annotations

import logging


class Runtime:
    """Controls the application runtime."""

    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger
        self._running = False

    @property
    def is_running(self) -> bool:
        """Return the runtime state."""
        return self._running

    def start(self) -> None:
        """Start the runtime."""
        self._running = True
        self._logger.info("Runtime started.")

    def stop(self) -> None:
        """Stop the runtime."""
        self._running = False
        self._logger.info("Runtime stopped.")
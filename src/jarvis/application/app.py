"""
Application entry point.
"""

from __future__ import annotations

from jarvis.application.bootstrap import Bootstrap
from jarvis.config.settings import Settings
from jarvis.core import Runtime


class JarvisApplication:
    """Main application."""

    def __init__(self) -> None:
        container = Bootstrap().build()

        self._runtime = container.get(Runtime)
        self._settings = container.get(Settings)

    def run(self) -> None:
        """Run the application."""

        self._runtime.start()

        try:
            input("JARVIS > ")
        finally:
            self._runtime.stop()
"""
Application bootstrap.
"""

from __future__ import annotations

from jarvis.config.settings import Settings
from jarvis.core import Runtime, ServiceContainer
from jarvis.utils.logger import create_logger


class Bootstrap:
    """Creates and configures the application."""

    def build(self) -> ServiceContainer:
        """Build the service container."""

        container = ServiceContainer()

        settings = Settings()
        logger = create_logger(settings.log_directory)
        runtime = Runtime(logger)

        container.register_instance(Settings, settings)
        container.register_instance(type(logger), logger)
        container.register_instance(Runtime, runtime)

        return container
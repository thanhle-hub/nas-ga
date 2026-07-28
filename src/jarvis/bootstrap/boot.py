"""
JARVIS boot sequence.
"""

from __future__ import annotations


from jarvis.config import ConfigLoader

from jarvis.logging import JarvisLogger

from jarvis.core import ServiceContainer

from jarvis.plugins import (
    PluginLoader,
    PluginManager,
    PluginLifecycle,
)

from jarvis.events import EventBus



class JarvisBootstrap:
    """
    Responsible for starting JARVIS.
    """


    def __init__(self) -> None:

        self.container = None

        self.config = None

        self.logger = None



    def start(self) -> ServiceContainer:
        """
        Execute boot sequence.
        """


        print(
            "=" * 40
        )

        print(
            "       JARVIS OS STARTING"
        )

        print(
            "=" * 40
        )



        # 1. Load configuration

        print(
            "[1] Loading configuration..."
        )


        self.config = (
            ConfigLoader()
            .load()
        )



        # 2. Initialize logger

        print(
            "[2] Initializing logger..."
        )


        self.logger = (
            JarvisLogger()
            .get_logger()
        )


        self.logger.info(
            "Logger initialized"
        )



        # 3. Create container

        print(
            "[3] Creating service container..."
        )


        self.container = (
            ServiceContainer()
        )



        # 4. Register services

        print(
            "[4] Registering services..."
        )


        self.container.register_instance(
            type(self.config),
            self.config,
        )


        self.container.register_instance(
            type(self.logger),
            self.logger,
        )



        # 5. Initialize event system

        event_bus = EventBus()


        self.container.register_instance(
            EventBus,
            event_bus,
        )



        # 6. Load plugins

        print(
            "[5] Loading plugins..."
        )


        plugin_manager = PluginManager(
            event_bus
        )


        plugin_loader = PluginLoader(
            self.config.plugins.directory
        )


        lifecycle = PluginLifecycle(
            plugin_manager,
            plugin_loader,
        )


        lifecycle.start()



        print(
            "=" * 40
        )

        print(
            "       JARVIS READY"
        )

        print(
            "=" * 40
        )


        return self.container
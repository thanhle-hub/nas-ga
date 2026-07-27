"""
Plugin lifecycle manager.
"""

from __future__ import annotations

from jarvis.events import (
    Event,
    EventBus,
    EventType,
)

from .base import Plugin
from .registry import PluginRegistry


class PluginManager:
    """
    Controls plugin lifecycle.
    """


    def __init__(
        self,
        event_bus: EventBus | None = None,
    ) -> None:

        self.registry = PluginRegistry()

        self.event_bus = event_bus



    def load(
        self,
        plugin: Plugin,
    ) -> None:
        """
        Load and activate plugin.
        """

        plugin.activate()

        self.registry.register(
            plugin
        )


        if self.event_bus:

            self.event_bus.publish(
                Event(
                    type=EventType.PLUGIN_LOADED,
                    payload={
                        "plugin": plugin.name
                    },
                )
            )



    def unload(
        self,
        name: str,
    ) -> None:
        """
        Stop plugin.
        """

        plugin = self.registry.get(
            name
        )


        if plugin is None:
            return


        plugin.deactivate()


        if self.event_bus:

            self.event_bus.publish(
                Event(
                    type=EventType.PLUGIN_STOPPED,
                    payload={
                        "plugin": name
                    },
                )
            )



    def load_all(
        self,
        plugins: list[Plugin],
    ) -> None:
        """
        Load multiple plugins.
        """

        for plugin in plugins:
            self.load(plugin)



    def plugins(
        self,
    ) -> list[Plugin]:
        """
        Return active plugins.
        """

        return self.registry.all()  
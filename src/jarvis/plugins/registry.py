"""
Plugin registry.
"""

from __future__ import annotations

from .base import Plugin


class PluginRegistry:
    """
    Stores loaded plugins.
    """


    def __init__(self) -> None:
        self._plugins: dict[str, Plugin] = {}


    def register(
        self,
        plugin: Plugin,
    ) -> None:
        """
        Register plugin.
        """

        self._plugins[plugin.name] = plugin


    def get(
        self,
        name: str,
    ) -> Plugin | None:
        """
        Get plugin by name.
        """

        return self._plugins.get(name)


    def all(
        self,
    ) -> list[Plugin]:
        """
        Return all plugins.
        """

        return list(
            self._plugins.values()
        )


    def count(
        self,
    ) -> int:
        """
        Return plugin count.
        """

        return len(self._plugins)
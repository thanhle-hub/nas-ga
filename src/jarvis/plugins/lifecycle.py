"""
Plugin lifecycle controller.
"""

from __future__ import annotations

from .loader import PluginLoader
from .manager import PluginManager


class PluginLifecycle:
    """
    Coordinates loading plugins.
    """


    def __init__(
        self,
        manager: PluginManager,
        loader: PluginLoader,
    ) -> None:

        self.manager = manager
        self.loader = loader



    def start(
        self,
    ) -> None:
        """
        Discover and load plugins.
        """

        plugins = self.loader.discover()

        self.manager.load_all(
            plugins
        )
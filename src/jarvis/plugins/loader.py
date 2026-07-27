"""
Plugin auto discovery system.
"""

from __future__ import annotations

import importlib.util
import inspect
from pathlib import Path

from .base import Plugin


class PluginLoader:
    """
    Discover plugins from external directory.
    """


    def __init__(
        self,
        plugin_path: str = "plugins",
    ) -> None:

        self.plugin_path = Path(plugin_path)


    def discover(self) -> list[Plugin]:
        """
        Discover and create plugin instances.
        """

        plugins: list[Plugin] = []

        if not self.plugin_path.exists():
            return plugins


        for folder in self.plugin_path.iterdir():

            if not folder.is_dir():
                continue


            plugin_file = folder / "plugin.py"


            if not plugin_file.exists():
                continue


            plugin = self._load_plugin(
                plugin_file
            )


            if plugin:
                plugins.append(plugin)


        return plugins



    def _load_plugin(
        self,
        file: Path,
    ) -> Plugin | None:
        """
        Load plugin from python file.
        """

        spec = importlib.util.spec_from_file_location(
            file.stem,
            file,
        )


        if spec is None or spec.loader is None:
            return None


        module = importlib.util.module_from_spec(
            spec
        )


        spec.loader.exec_module(module)


        for _, obj in inspect.getmembers(
            module,
            inspect.isclass,
        ):

            if (
                issubclass(obj, Plugin)
                and obj is not Plugin
            ):
                return obj()


        return None
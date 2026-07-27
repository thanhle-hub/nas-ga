from pathlib import Path

from jarvis.plugins import (
    PluginLoader,
)


def test_plugin_discovery(tmp_path: Path):

    plugin_dir = tmp_path / "plugins"

    calculator = plugin_dir / "calculator"

    calculator.mkdir(
        parents=True
    )


    file = calculator / "plugin.py"


    file.write_text(
        """
from jarvis.plugins import Plugin


class CalculatorPlugin(Plugin):

    name = "calculator"


    def activate(self):
        pass


    def deactivate(self):
        pass
"""
    )


    loader = PluginLoader(
        str(plugin_dir)
    )


    plugins = loader.discover()


    assert len(plugins) == 1

    assert plugins[0].name == "calculator"
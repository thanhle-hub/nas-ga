from jarvis.plugins import (
    Plugin,
    PluginManager,
)


class DummyPlugin(Plugin):

    name = "dummy"


    def __init__(self) -> None:
        self.active = False


    def activate(self) -> None:
        self.active = True


    def deactivate(self) -> None:
        self.active = False



def test_plugin_load():

    manager = PluginManager()

    plugin = DummyPlugin()

    manager.load(plugin)


    assert manager.registry.count() == 1

    assert plugin.active is True
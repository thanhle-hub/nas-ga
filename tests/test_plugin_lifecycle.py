from jarvis.events import (
    EventBus,
    EventType,
)

from jarvis.plugins import (
    Plugin,
    PluginLoader,
    PluginManager,
    PluginLifecycle,
)



class DummyLifecyclePlugin(Plugin):

    name = "lifecycle_test"


    def __init__(self):
        self.started = False


    def activate(self):
        self.started = True


    def deactivate(self):
        self.started = False



def test_plugin_lifecycle():

    bus = EventBus()

    manager = PluginManager(
        bus
    )

    loader = PluginLoader()

    lifecycle = PluginLifecycle(
        manager,
        loader,
    )


    plugin = DummyLifecyclePlugin()

    manager.load(plugin)


    assert manager.registry.count() == 1

    assert plugin.started is True
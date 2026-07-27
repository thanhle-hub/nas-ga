from jarvis.config import ConfigLoader



def test_config_loading():

    config = ConfigLoader().load()


    assert config.system.name == "JARVIS"


    assert (
        config.plugins.directory
        == "plugins"
    )


    assert config.ai.provider == "ollama"
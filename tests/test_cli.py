from jarvis.commands import CommandRouter

from jarvis.interface import CLIInterface



def test_cli_creation():

    router = CommandRouter()


    cli = CLIInterface(
        router
    )


    assert cli.running is True

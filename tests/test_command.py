from jarvis.commands import (
    CommandParser,
    CommandRouter,
)



def test_command_parser():

    parser = CommandParser()


    command = parser.parse(
        "hello jarvis"
    )


    assert command.name == "hello"

    assert command.args == [
        "jarvis"
    ]



def test_command_router():

    router = CommandRouter()


    router.register(
        "hello",
        lambda cmd:
            "Hello user"
    )


    result = router.execute(
        CommandParser().parse(
            "hello"
        )
    )


    assert result == "Hello user"
from jarvis.memory import (
    MemoryManager,
    MemoryCommands,
)

from jarvis.commands import (
    CommandParser,
)



def test_remember_command(
    tmp_path,
):

    storage_file = (
        tmp_path /
        "memory.json"
    )


    from jarvis.memory import MemoryStorage


    storage = MemoryStorage(
        str(storage_file)
    )


    memory = MemoryManager(
        storage
    )


    commands = MemoryCommands(
        memory
    )


    parser = CommandParser()


    result = commands.remember(
        parser.parse(
            "remember name Minh"
        )
    )


    assert (
        result ==
        "I remembered name = Minh"
    )


    assert (
        memory.recall("name")
        ==
        "Minh"
    )
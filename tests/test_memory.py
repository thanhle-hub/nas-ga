from jarvis.memory import (
    MemoryStorage,
    MemoryManager,
)



def test_memory_save_and_load(
    tmp_path,
):

    file = (
        tmp_path /
        "memory.json"
    )


    storage = MemoryStorage(
        str(file)
    )


    memory = MemoryManager(
        storage
    )


    memory.remember(
        "name",
        "Minh",
    )


    result = memory.recall(
        "name"
    )


    assert result == "Minh"
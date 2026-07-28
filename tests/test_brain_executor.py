from jarvis.brain import (
    Brain,
    BrainExecutor,
)

from jarvis.memory import (
    MemoryManager,
    MemoryStorage,
)



def test_brain_executor_remember(
    tmp_path,
):

    storage = MemoryStorage(
        str(
            tmp_path /
            "memory.json"
        )
    )


    memory = MemoryManager(
        storage
    )


    brain = Brain()

    executor = BrainExecutor(
        memory
    )


    intent = brain.think(
        "My name is Minh"
    )


    result = executor.execute(
        intent
    )


    assert (
        result ==
        "I will remember your name."
    )


    assert (
        memory.recall("name")
        ==
        "minh"
    )
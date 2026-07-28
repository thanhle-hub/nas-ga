from jarvis.brain import (
    Brain,
    BrainExecutor,
    BrainPipeline,
)

from jarvis.memory import (
    MemoryManager,
    MemoryStorage,
)



def test_pipeline_memory(
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


    pipeline = BrainPipeline(
        Brain(),
        BrainExecutor(memory),
    )


    response = pipeline.process(
        "My name is Minh"
    )


    assert (
        response ==
        "I will remember your name."
    )


    response = pipeline.process(
        "What is my name?"
    )


    assert (
        response ==
        "Your name is minh."
    )
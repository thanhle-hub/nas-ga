from jarvis.brain import (
    Brain,
    BrainExecutor,
    BrainRouter,
    LLMHandler,
)

from jarvis.memory import (
    MemoryManager,
    MemoryStorage,
)

from jarvis.llm import MockLLM



def test_rule_route(
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


    router = BrainRouter(

        Brain(),

        BrainExecutor(
            memory
        ),

        LLMHandler(
            MockLLM()
        )
    )


    result = router.process(
        "My name is Minh"
    )


    assert (
        result ==
        "I will remember your name."
    )



def test_llm_route(
    tmp_path,
):

    memory = MemoryManager(
        MemoryStorage(
            str(
                tmp_path /
                "memory.json"
            )
        )
    )


    router = BrainRouter(

        Brain(),

        BrainExecutor(
            memory
        ),

        LLMHandler(
            MockLLM()
        )
    )


    result = router.process(
        "Explain robotics"
    )


    assert (
        "LLM response:"
        in result
    )
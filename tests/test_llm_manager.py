from jarvis.llm import (
    MockLLM,
    LLMManager,
)


def test_llm():

    manager = LLMManager(
        MockLLM()
    )

    response = manager.ask(
        "Hello"
    )

    assert (
        response.text
        ==
        "LLM response: Hello"
    )

    assert (
        response.model
        ==
        "mock"
    )
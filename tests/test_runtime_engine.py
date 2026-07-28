from jarvis.runtime import (
    AgentRuntime,
    AgentSession,
)

from jarvis.llm import (
    MockLLM,
    LLMManager,
)


def test_runtime_engine():

    runtime = AgentRuntime(

        LLMManager(
            MockLLM()
        )

    )

    session = AgentSession()

    answer = runtime.ask(

        session,

        "Hello",

    )

    assert "LLM response:" in answer

    assert len(
        session.history()
    ) == 2

    assert (
        session.history()[0].role
        ==
        "user"
    )

    assert (
        session.history()[1].role
        ==
        "assistant"
    )
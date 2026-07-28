from jarvis.llm import (
    LLMConfig,
    LLMFactory,
    MockLLM,
    OpenAIClient,
    OllamaClient,
)


def test_mock_factory():

    llm = LLMFactory.create(
        LLMConfig(provider="mock")
    )

    assert isinstance(
        llm,
        MockLLM,
    )


def test_openai_factory():

    llm = LLMFactory.create(

        LLMConfig(

            provider="openai",

            model="gpt-5.5",

        )

    )

    assert isinstance(

        llm,

        OpenAIClient,

    )


def test_ollama_factory():

    llm = LLMFactory.create(

        LLMConfig(

            provider="ollama",

            model="llama3",

        )

    )

    assert isinstance(

        llm,

        OllamaClient,

    )
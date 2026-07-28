from jarvis.runtime import (
    Conversation,
    PromptBuilder,
)


def test_prompt_builder():

    conversation = Conversation()

    conversation.add(
        "user",
        "Hello",
    )

    conversation.add(
        "assistant",
        "Hi!",
    )

    prompt = PromptBuilder().build(

        conversation,

        system_prompt="You are Jarvis.",

    )

    assert "System:" in prompt

    assert "User: Hello" in prompt

    assert "Assistant: Hi!" in prompt
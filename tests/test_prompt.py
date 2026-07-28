from jarvis.llm import (
    PromptContext,
    PromptBuilder,
)



def test_prompt_builder():


    context = PromptContext(

        user_input=
        "What is my name?",

        memory={
            "name": "Minh"
        },

        history=[
            "User: My name is Minh"
        ]
    )


    builder = PromptBuilder()


    prompt = builder.build(
        context
    )


    assert (
        "SYSTEM:"
        in prompt
    )


    assert (
        "name: Minh"
        in prompt
    )


    assert (
        "What is my name?"
        in prompt
    )
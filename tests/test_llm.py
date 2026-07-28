from jarvis.llm import (
    MockLLM,
)



def test_mock_llm():

    llm = MockLLM()


    result = llm.generate(
        "hello"
    )


    assert (
        result
        ==
        "LLM response: hello"
    )

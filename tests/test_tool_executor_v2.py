from jarvis.tools import (
    ToolDescriptor,
    ToolExecutor,
)


def hello():

    return "hello"


def test_tool_executor():

    descriptor = ToolDescriptor(

        name="hello",

        description="Greeting",

        function=hello,

    )


    executor = ToolExecutor()


    result = executor.execute(
        descriptor
    )


    assert result.success

    assert result.output == "hello"
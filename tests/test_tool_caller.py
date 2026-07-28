from jarvis.tools import (
    ToolRegistry,
    ToolCaller,
)


def calculator():

    return 100


def test_tool_caller():

    registry = ToolRegistry()

    registry.register(

        name="calculator",

        function=calculator,

        description="Calculator",

        tags=["math"],

    )


    caller = ToolCaller(
        registry
    )


    result = caller.call(
        "calculator"
    )


    assert result.success

    assert result.output == 100
from jarvis.plugins import (
    Tool,
    ToolRegistry,
)


def calculator(
    text
):

    return "42"



def test_tool_registry():


    registry = ToolRegistry()


    tool = Tool(
        name="calculator",
        description=
        "calculate numbers",
        handler=calculator,
    )


    registry.register(
        tool
    )


    result = registry.get(
        "calculator"
    )


    assert result is tool



def test_tool_execute():


    tool = Tool(
        name="calculator",
        description="calculate",
        handler=calculator,
    )


    assert (
        tool.execute("")
        ==
        "42"
    )
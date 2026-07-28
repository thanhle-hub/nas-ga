from jarvis.plugins import (
    Tool,
    ToolRegistry,
    ToolExecutor,
)


from jarvis.plugins.builtin import (
    calculator,
)



def test_tool_execution():


    registry = ToolRegistry()


    registry.register(
        Tool(
            name="calculator",
            description=
            "calculate numbers",
            handler=calculator,
        )
    )


    executor = ToolExecutor(
        registry
    )


    result = executor.execute(
        "calculator",
        "20+30"
    )


    assert (
        result == "50"
    )
from jarvis.tools import (
    ToolRegistry,
    ToolSelector,
)


def calculator():

    return 42


def weather():

    return "sunny"


def test_select_by_name():

    registry = ToolRegistry()

    registry.register(
        name="calculator",
        function=calculator,
        description="Math calculator",
        tags=["math"],
    )

    selector = ToolSelector(
        registry
    )

    tool = selector.select(
        "calculator"
    )

    assert tool is not None

    assert tool.name == "calculator"


def test_select_by_tag():

    registry = ToolRegistry()

    registry.register(
        name="calculator",
        function=calculator,
        description="Math calculator",
        tags=["math"],
    )

    selector = ToolSelector(
        registry
    )

    tool = selector.select(
        "math"
    )

    assert tool is not None

    assert tool.name == "calculator"


def test_select_by_description():

    registry = ToolRegistry()

    registry.register(
        name="weather",
        function=weather,
        description="Weather forecast service",
        tags=["forecast"],
    )

    selector = ToolSelector(
        registry
    )

    tool = selector.select(
        "weather"
    )

    assert tool is not None

    assert tool.name == "weather"
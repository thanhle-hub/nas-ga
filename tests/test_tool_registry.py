from jarvis.tools import ToolRegistry


def hello():
    return "hello"


def test_tool_descriptor():

    registry = ToolRegistry()

    registry.register(
        name="hello",
        function=hello,
        description="Greeting tool",
        tags=["demo", "text"],
    )

    tool = registry.get("hello")

    assert tool is not None
    assert tool.name == "hello"
    assert tool.description == "Greeting tool"
    assert "demo" in tool.tags
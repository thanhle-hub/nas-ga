"""
Tool execution system.
"""

from .tool_registry import ToolRegistry



class ToolExecutor:
    """
    Execute registered tools.
    """


    def __init__(
        self,
        registry: ToolRegistry,
    ) -> None:

        self.registry = registry



    def execute(
        self,
        tool_name: str,
        *args,
        **kwargs,
    ) -> str:
        """
        Execute tool by name.
        """


        tool = (
            self.registry.get(
                tool_name
            )
        )


        if tool is None:

            raise ValueError(
                f"Tool not found: {tool_name}"
            )


        return tool.execute(
            *args,
            **kwargs
        )
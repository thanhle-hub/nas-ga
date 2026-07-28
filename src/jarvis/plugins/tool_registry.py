"""
Tool registry.
"""

from .tool import Tool



class ToolRegistry:
    """
    Store available tools.
    """


    def __init__(self):

        self.tools = {}



    def register(
        self,
        tool: Tool,
    ):

        self.tools[
            tool.name
        ] = tool



    def get(
        self,
        name: str,
    ) -> Tool | None:

        return self.tools.get(
            name
        )



    def list_tools(
        self,
    ):

        return list(
            self.tools.values()
        )
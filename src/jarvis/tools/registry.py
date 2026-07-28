from .descriptor import ToolDescriptor


class ToolRegistry:

    def __init__(self):

        self._tools: dict[str, ToolDescriptor] = {}


    def register(
        self,
        name: str,
        function,
        description: str = "",
        tags: list[str] | None = None,
    ):

        self._tools[name] = ToolDescriptor(
            name=name,
            description=description,
            function=function,
            tags=tags or [],
        )


    def get(
        self,
        name: str,
    ) -> ToolDescriptor | None:

        return self._tools.get(name)


    def list_tools(self):

        return list(self._tools.values())
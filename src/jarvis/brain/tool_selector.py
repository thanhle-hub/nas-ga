"""
Select tools based on user input.
"""

from jarvis.plugins import ToolRegistry



class ToolSelector:
    """
    Simple rule-based tool selector.
    """


    def __init__(
        self,
        registry: ToolRegistry,
    ):

        self.registry = registry



    def select(
        self,
        text: str,
    ):


        text = text.lower()



        for tool in (
            self.registry.list_tools()
        ):

            keywords = (
                tool.description
                .lower()
                .split()
            )


            for keyword in keywords:

                if keyword in text:

                    return tool



        return None
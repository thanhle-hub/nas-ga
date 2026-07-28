"""
Tool pipeline.
"""

from jarvis.plugins import (
    ToolExecutor,
)

from .tool_selector import ToolSelector



class ToolPipeline:
    """
    Select and execute tools.
    """



    def __init__(
        self,
        selector: ToolSelector,
        executor: ToolExecutor,
    ):

        self.selector = selector

        self.executor = executor



    def process(
        self,
        text: str,
    ):


        tool = (
            self.selector
            .select(text)
        )


        if tool is None:

            return None



        return self.executor.execute(
            tool.name,
            text,
        )
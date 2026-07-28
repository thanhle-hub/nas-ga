"""
Tool caller.
"""

from __future__ import annotations

from .executor import ToolExecutor
from .registry import ToolRegistry
from .selector import ToolSelector
from .result import ToolResult


class ToolCaller:
    """
    High-level tool calling interface.
    """

    def __init__(
        self,
        registry: ToolRegistry,
    ) -> None:

        self.registry = registry

        self.selector = ToolSelector(
            registry
        )

        self.executor = ToolExecutor()


    def call(
        self,
        action: str,
        *args,
        **kwargs,
    ) -> ToolResult:

        tool = self.selector.select(
            action
        )

        if tool is None:

            return ToolResult(
                success=False,
                error=f"No tool found for '{action}'",
            )

        return self.executor.execute(
            tool,
            *args,
            **kwargs,
        )
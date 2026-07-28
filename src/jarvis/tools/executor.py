"""
Tool executor.
"""

from __future__ import annotations

from .descriptor import ToolDescriptor
from .result import ToolResult


class ToolExecutor:
    """
    Execute a registered tool.
    """

    def execute(
        self,
        tool: ToolDescriptor,
        *args,
        **kwargs,
    ) -> ToolResult:

        try:

            output = tool.function(
                *args,
                **kwargs,
            )

            return ToolResult(
                success=True,
                output=output,
            )

        except Exception as exc:

            return ToolResult(
                success=False,
                error=str(exc),
            )
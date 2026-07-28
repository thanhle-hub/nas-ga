"""
Tool execution result.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ToolResult:
    """
    Result returned by a tool execution.
    """

    success: bool

    output: object | None = None

    error: str | None = None
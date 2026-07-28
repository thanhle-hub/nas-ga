"""
Tool descriptor.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ToolDescriptor:
    """
    Metadata describing a tool.
    """

    name: str

    description: str

    function: callable

    tags: list[str] = field(default_factory=list)
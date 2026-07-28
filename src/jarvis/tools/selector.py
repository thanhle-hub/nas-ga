"""
Tool selector.
"""

from __future__ import annotations

from .registry import ToolRegistry
from .descriptor import ToolDescriptor


class ToolSelector:
    """
    Select the best tool for a requested action.
    """

    def __init__(
        self,
        registry: ToolRegistry,
    ) -> None:

        self.registry = registry


    def select(
        self,
        action: str,
    ) -> ToolDescriptor | None:

        action = action.lower()

        #
        # Exact name match
        #
        tool = self.registry.get(action)

        if tool is not None:
            return tool

        #
        # Tag match
        #
        for tool in self.registry.list_tools():

            if action in tool.tags:
                return tool

        #
        # Description keyword match
        #
        for tool in self.registry.list_tools():

            if action in tool.description.lower():
                return tool

        return None
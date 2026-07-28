"""
Unified agent context.
"""

from dataclasses import dataclass, field



@dataclass
class AgentContext:
    """
    Combined memory and knowledge context.
    """


    memories: list[str] = field(
        default_factory=list
    )


    knowledge: list[str] = field(
        default_factory=list
    )
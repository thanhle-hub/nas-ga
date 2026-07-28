"""
Command data model.
"""

from dataclasses import dataclass


@dataclass
class Command:
    """
    Represents a user command.
    """

    name: str

    args: list[str]


    def has_args(self) -> bool:
        """
        Check command arguments.
        """

        return len(self.args) > 0
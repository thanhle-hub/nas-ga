"""
Intent model.
"""

from dataclasses import dataclass


@dataclass
class Intent:
    """
    Represents user intention.
    """

    name: str

    entities: dict


    def has_entities(self) -> bool:
        return len(self.entities) > 0
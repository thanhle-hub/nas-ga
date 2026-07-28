"""
Knowledge document model.
"""

from dataclasses import dataclass



@dataclass
class Document:
    """
    Represents a knowledge document.
    """


    title: str

    content: str
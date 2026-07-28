"""
Reasoning thought model.
"""

from dataclasses import dataclass



@dataclass
class Thought:
    """
    Represents reasoning step.
    """


    observation: str

    conclusion: str
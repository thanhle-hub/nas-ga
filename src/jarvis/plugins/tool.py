"""
Tool definition model.
"""

from dataclasses import dataclass
from typing import Callable



@dataclass
class Tool:

    """
    Represents a JARVIS tool.
    """


    name: str

    description: str

    handler: Callable



    def execute(
        self,
        *args,
        **kwargs,
    ):

        return self.handler(
            *args,
            **kwargs
        )
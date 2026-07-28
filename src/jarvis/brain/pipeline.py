"""
JARVIS brain pipeline.
"""

from __future__ import annotations

from .brain import Brain
from .executor import BrainExecutor



class BrainPipeline:
    """
    Complete reasoning pipeline.

    Input:
        user text

    Output:
        response
    """


    def __init__(
        self,
        brain: Brain,
        executor: BrainExecutor,
    ) -> None:

        self.brain = brain

        self.executor = executor



    def process(
        self,
        text: str,
    ) -> str:
        """
        Process user input.
        """


        intent = (
            self.brain.think(
                text
            )
        )


        response = (
            self.executor.execute(
                intent
            )
        )


        return response
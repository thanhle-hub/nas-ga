"""
Hybrid brain router.
"""

from .brain import Brain
from .executor import BrainExecutor
from .llm_handler import LLMHandler



class BrainRouter:
    """
    Decide between rules and LLM.
    """


    def __init__(
        self,
        brain: Brain,
        executor: BrainExecutor,
        llm_handler: LLMHandler,
    ) -> None:

        self.brain = brain

        self.executor = executor

        self.llm_handler = llm_handler



    def process(
        self,
        text: str,
    ) -> str:


        intent = (
            self.brain.think(text)
        )


        if (
            intent.name
            !=
            "unknown"
        ):

            return (
                self.executor
                .execute(intent)
            )


        return (
            self.llm_handler
            .handle(text)
        )
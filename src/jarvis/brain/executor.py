"""
Brain executor.
"""

from __future__ import annotations

from jarvis.memory import MemoryManager

from .intent import Intent



class BrainExecutor:
    """
    Execute actions based on intent.
    """


    def __init__(
        self,
        memory: MemoryManager,
    ) -> None:

        self.memory = memory



    def execute(
        self,
        intent: Intent,
    ) -> str:
        """
        Execute intent.
        """


        if intent.name == "remember":

            key = (
                intent.entities["key"]
            )

            value = (
                intent.entities["value"]
            )


            self.memory.remember(
                key,
                value,
            )


            return (
                f"I will remember "
                f"your {key}."
            )



        if intent.name == "recall":

            key = (
                intent.entities["key"]
            )


            value = (
                self.memory.recall(
                    key
                )
            )


            if value:

                return (
                    f"Your {key} is {value}."
                )


            return (
                f"I don't know your {key}."
            )



        if intent.name == "hello":

            return (
                "Hello. How can I help you?"
            )



        return (
            "I don't understand."
        )
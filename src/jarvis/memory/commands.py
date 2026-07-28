"""
Memory command handlers.
"""

from .memory import MemoryManager



class MemoryCommands:
    """
    JARVIS memory related commands.
    """


    def __init__(
        self,
        memory: MemoryManager,
    ) -> None:

        self.memory = memory



    def remember(
        self,
        command,
    ) -> str:
        """
        Store information.

        Example:
            remember name Minh
        """


        if len(command.args) < 2:

            return (
                "Usage: remember key value"
            )


        key = command.args[0]

        value = " ".join(
            command.args[1:]
        )


        self.memory.remember(
            key,
            value,
        )


        return (
            f"I remembered {key} = {value}"
        )



    def recall(
        self,
        command,
    ) -> str:
        """
        Retrieve information.

        Example:
            recall name
        """


        if len(command.args) < 1:

            return (
                "Usage: recall key"
            )


        key = command.args[0]


        value = self.memory.recall(
            key
        )


        if value is None:

            return (
                f"I don't know {key}"
            )


        return (
            f"{key} is {value}"
        )
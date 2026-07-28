"""
Command router.
"""

from collections.abc import Callable

from .command import Command



class CommandRouter:
    """
    Routes commands to handlers.
    """


    def __init__(self):

        self.handlers = {}



    def register(
        self,
        command: str,
        handler: Callable,
    ) -> None:
        """
        Register command handler.
        """

        self.handlers[
            command
        ] = handler



    def execute(
        self,
        command: Command,
    ):

        handler = (
            self.handlers.get(
                command.name
            )
        )


        if handler is None:

            return (
                f"Unknown command: "
                f"{command.name}"
            )


        return handler(
            command
        )
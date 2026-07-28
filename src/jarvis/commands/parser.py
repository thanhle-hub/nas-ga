"""
Command parser.
"""

from .command import Command



class CommandParser:
    """
    Convert text input into Command.
    """


    def parse(
        self,
        text: str,
    ) -> Command:
        """
        Parse user text.
        """


        parts = (
            text
            .strip()
            .split()
        )


        if not parts:

            return Command(
                name="",
                args=[],
            )


        return Command(
            name=parts[0].lower(),
            args=parts[1:],
        )
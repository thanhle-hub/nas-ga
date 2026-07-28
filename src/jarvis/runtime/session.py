"""
Agent session.
"""

from __future__ import annotations

from uuid import uuid4

from .conversation import Conversation


class AgentSession:
    """
    Represents one user session.
    """

    def __init__(self):

        self.id = str(uuid4())

        self.conversation = Conversation()

        self.metadata = {}


    def add_user_message(
        self,
        text: str,
    ):

        self.conversation.add(
            "user",
            text,
        )


    def add_assistant_message(
        self,
        text: str,
    ):

        self.conversation.add(
            "assistant",
            text,
        )


    def history(self):

        return self.conversation.messages()
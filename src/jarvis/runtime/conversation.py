"""
Conversation history.
"""

from __future__ import annotations

from .message import Message


class Conversation:

    def __init__(self):

        self._messages: list[Message] = []


    def add(

        self,

        role: str,

        content: str,

    ) -> None:

        self._messages.append(

            Message(

                role=role,

                content=content,

            )

        )


    def messages(self):

        return list(

            self._messages

        )


    def last(self):

        if not self._messages:

            return None

        return self._messages[-1]


    def clear(self):

        self._messages.clear()


    def __len__(self):

        return len(

            self._messages

        )
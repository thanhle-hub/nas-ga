"""
Conversation context memory.
"""

from dataclasses import dataclass, field



@dataclass
class ConversationContext:
    """
    Stores current conversation.
    """


    history: list[dict] = field(
        default_factory=list
    )



    def add(
        self,
        role: str,
        message: str,
    ) -> None:

        self.history.append(
            {
                "role": role,
                "message": message,
            }
        )



    def clear(self):

        self.history.clear()
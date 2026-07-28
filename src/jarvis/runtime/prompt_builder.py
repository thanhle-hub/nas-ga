"""
Prompt builder.
"""

from __future__ import annotations

from .conversation import Conversation


class PromptBuilder:
    """
    Build prompts for the LLM from conversation history.
    """

    def build(
        self,
        conversation: Conversation,
        system_prompt: str = "",
    ) -> str:

        lines = []

        if system_prompt:

            lines.append(
                f"System: {system_prompt}"
            )

            lines.append("")

        for message in conversation.messages():

            lines.append(

                f"{message.role.capitalize()}: {message.content}"

            )

        return "\n".join(lines)
"""
Agent runtime.
"""

from __future__ import annotations

from jarvis.llm import LLMManager

from .session import AgentSession
from .prompt_builder import PromptBuilder


class AgentRuntime:
    """
    Main runtime coordinating a conversation with an LLM.
    """

    def __init__(
        self,
        llm: LLMManager,
    ) -> None:

        self.llm = llm

        self.builder = PromptBuilder()


    def ask(
        self,
        session: AgentSession,
        user_input: str,
        system_prompt: str = "You are Jarvis.",
    ) -> str:

        #
        # Add user message
        #
        session.add_user_message(
            user_input
        )

        #
        # Build prompt
        #
        prompt = self.builder.build(
            session.conversation,
            system_prompt=system_prompt,
        )

        #
        # Ask LLM
        #
        response = self.llm.ask(
            prompt
        )

        #
        # Save assistant reply
        #
        session.add_assistant_message(
            response.text
        )

        #
        # Return text
        #
        return response.text
"""
Prompt context model.
"""

from dataclasses import dataclass, field



@dataclass
class PromptContext:
    """
    Information used to build LLM prompt.
    """


    system: str = (
        "You are JARVIS, "
        "an intelligent assistant."
    )


    user_input: str = ""


    memory: dict = field(
        default_factory=dict
    )


    history: list[str] = field(
        default_factory=list
    )
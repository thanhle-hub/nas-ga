"""
LLM handler for complex requests.
"""

from jarvis.llm import (
    LLMProvider,
    PromptBuilder,
    PromptContext,
)



class LLMHandler:
    """
    Handle requests using LLM.
    """


    def __init__(
        self,
        llm: LLMProvider,
    ) -> None:

        self.llm = llm

        self.prompt_builder = (
            PromptBuilder()
        )



    def handle(
        self,
        text: str,
        memory: dict | None = None,
    ) -> str:
        """
        Generate LLM response.
        """


        context = PromptContext(

            user_input=text,

            memory=(
                memory
                or {}
            )
        )


        prompt = (
            self.prompt_builder
            .build(context)
        )


        return self.llm.generate(
            prompt
        )
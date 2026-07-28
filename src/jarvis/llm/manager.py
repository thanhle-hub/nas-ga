from .base import BaseLLM


class LLMManager:

    def __init__(
        self,
        llm: BaseLLM,
    ):

        self.llm = llm


    def ask(
        self,
        prompt: str,
    ):

        return self.llm.generate(
            prompt
        )
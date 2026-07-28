from .base import BaseLLM
from .response import LLMResponse


class MockLLM(BaseLLM):

    def generate(
        self,
        prompt: str,
    ) -> LLMResponse:

        return LLMResponse(

            text=f"LLM response: {prompt}",

            model="mock",

        )
"""
LLM provider interface.
"""

from abc import ABC, abstractmethod



class LLMProvider(ABC):
    """
    Abstract LLM interface.
    """


    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate response.
        """

        pass
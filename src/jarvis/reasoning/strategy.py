"""
Reasoning strategy.
"""



class ReasoningStrategy:
    """
    Decide reasoning approach.
    """



    def decide(
        self,
        query: str,
    ) -> str:


        if len(query.split()) > 5:

            return "complex"


        return "simple"
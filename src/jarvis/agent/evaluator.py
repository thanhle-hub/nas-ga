"""
Agent evaluation module.
"""



class Evaluator:
    """
    Evaluate execution result.
    """



    def evaluate(
        self,
        result: object,
    ) -> str:


        if result is None:

            return "failure"


        return "success"
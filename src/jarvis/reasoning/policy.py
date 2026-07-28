"""
Decision policy.
"""



class DecisionPolicy:
    """
    Select action based on reasoning.
    """



    def select(
        self,
        query: str,
    ) -> tuple[str, str]:


        text = query.lower()


        if "analyze" in text:

            return (
                "analyze_dataset",
                "Analysis task detected",
            )


        if "train" in text:

            return (
                "train_model",
                "Training task detected",
            )


        return (
            "answer_question",
            "General query",
        )
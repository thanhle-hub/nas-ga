"""
Reasoning engine with decision.
"""

from .thought import Thought

from .strategy import (
    ReasoningStrategy,
)

from .decision import (
    Decision,
)

from .policy import (
    DecisionPolicy,
)



class ReasoningEngine:



    def __init__(
        self,
        strategy=None,
        policy=None,
    ):


        self.strategy = (
            strategy
            or ReasoningStrategy()
        )


        self.policy = (
            policy
            or DecisionPolicy()
        )



    def reason(
        self,
        query: str,
    ) -> Thought:


        mode = (
            self.strategy
            .decide(query)
        )


        if mode == "complex":

            return Thought(
                observation=query,
                conclusion=
                "Use planning and execution"
            )


        return Thought(
            observation=query,
            conclusion=
            "Provide direct response"
        )



    def decide(
        self,
        query: str,
    ) -> Decision:


        action, reason = (
            self.policy
            .select(query)
        )


        return Decision(
            action=action,
            reason=reason,
        )
"""
Agent observation module.
"""


from dataclasses import dataclass



@dataclass
class Observation:
    """
    Represents current agent state.
    """

    input: str



class Observer:
    """
    Observe user goal.
    """

    def observe(
        self,
        goal: str,
    ) -> Observation:

        return Observation(
            input=goal
        )
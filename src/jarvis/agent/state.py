"""
Agent execution state.
"""

from __future__ import annotations

from dataclasses import dataclass, field



@dataclass
class AgentState:
    """
    Agent execution result.

    Supports:

    Legacy:
        state.finished
        state.result
        state.steps

    New:
        state["status"]
        state["result"]
    """


    finished: bool = False


    result: object | None = None


    status: str = "running"


    steps: list[str] = field(
        default_factory=list
    )



    def __getitem__(
        self,
        key: str,
    ):
        """
        Dictionary-style access.
        """

        if key == "finished":

            return self.finished


        if key == "result":

            return self.result


        if key == "status":

            return self.status


        if key == "steps":

            return self.steps


        raise KeyError(
            key
        )
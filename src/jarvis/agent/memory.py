"""
Agent memory with persistence.
"""

from dataclasses import dataclass, field

from jarvis.memory import AgentMemoryStore



@dataclass
class AgentMemory:
    """
    Stores agent execution memory.
    """


    store: AgentMemoryStore | None = None


    goals: list[str] = field(
        default_factory=list
    )


    tasks: list[str] = field(
        default_factory=list
    )


    results: list[str] = field(
        default_factory=list
    )



    def remember_goal(
        self,
        goal: str,
    ) -> None:

        self.goals.append(
            goal
        )


        if self.store:

            self.store.save(
                "last_goal",
                goal,
            )



    def remember_task(
        self,
        task: str,
    ) -> None:

        self.tasks.append(
            task
        )


        if self.store:

            self.store.save(
                "last_task",
                task,
            )



    def remember_result(
        self,
        result: str,
    ) -> None:

        self.results.append(
            result
        )


        if self.store:

            self.store.save(
                "last_result",
                result,
            )
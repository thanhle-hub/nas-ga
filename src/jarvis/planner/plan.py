"""
Plan model.
"""

from dataclasses import dataclass, field

from .task import Task



@dataclass
class Plan:
    """
    Collection of tasks.
    """


    goal: str


    tasks: list[Task] = field(
        default_factory=list
    )



    def add_task(
        self,
        task: Task,
    ):

        self.tasks.append(
            task
        )
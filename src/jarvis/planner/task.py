"""
Task model.
"""

from dataclasses import dataclass



@dataclass
class Task:
    """
    Represents one planning step.
    """


    name: str


    status: str = "pending"



    def complete(self):

        self.status = "completed"
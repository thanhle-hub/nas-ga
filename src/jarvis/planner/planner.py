"""
Planner engine.
"""

from .task import Task
from .plan import Plan



class Planner:
    """
    Create execution plans.
    """



    def create_plan(
        self,
        goal: str,
    ) -> Plan:


        plan = Plan(
            goal=goal
        )


        plan.add_task(
            Task(
                "Understand goal"
            )
        )


        plan.add_task(
            Task(
                "Execute required action"
            )
        )


        plan.add_task(
            Task(
                "Evaluate result"
            )
        )


        return plan
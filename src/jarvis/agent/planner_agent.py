"""
Planner based agent with memory.
"""

from jarvis.planner import (
    Planner,
    PlanExecutor,
)

from .memory import AgentMemory



class PlannerAgent:


    def __init__(
        self,
        planner: Planner,
        executor: PlanExecutor,
        memory: AgentMemory | None = None,
    ):

        self.planner = planner

        self.executor = executor

        self.memory = (
            memory
            or AgentMemory()
        )



    def run(
        self,
        goal: str,
    ):


        self.memory.remember_goal(
            goal
        )


        plan = (
            self.planner
            .create_plan(goal)
        )


        for task in plan.tasks:

            self.memory.remember_task(
                task.name
            )


        result = (
            self.executor
            .execute(plan)
        )


        self.memory.remember_result(
            "Plan completed"
        )


        return result
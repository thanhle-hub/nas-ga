"""
Plan execution system.
"""

from .plan import Plan



class PlanExecutor:
    """
    Execute tasks inside a plan.
    """



    def execute(
        self,
        plan: Plan,
    ) -> Plan:
        """
        Execute all tasks.
        """


        for task in plan.tasks:

            task.status = "running"


            # Placeholder execution
            # Later connected to AgentLoop


            task.complete()


        return plan
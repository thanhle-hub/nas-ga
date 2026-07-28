from jarvis.agent import (
    PlannerAgent,
)

from jarvis.planner import (
    Planner,
    PlanExecutor,
)



def test_planner_agent():


    agent = PlannerAgent(

        Planner(),

        PlanExecutor()

    )


    result = agent.run(
        "Analyze CPU dataset"
    )


    assert (
        len(result.tasks)
        ==
        3
    )


    for task in result.tasks:

        assert (
            task.status
            ==
            "completed"
        )

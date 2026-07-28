from jarvis.planner import (
    Planner,
    PlanExecutor,
)



def test_execute_plan():


    planner = Planner()


    plan = planner.create_plan(
        "Analyze CPU dataset"
    )


    executor = PlanExecutor()


    result = executor.execute(
        plan
    )


    for task in result.tasks:

        assert (
            task.status
            ==
            "completed"
        )
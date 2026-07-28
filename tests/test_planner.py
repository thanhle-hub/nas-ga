from jarvis.planner import (
    Planner,
    Task,
)



def test_create_plan():


    planner = Planner()


    plan = planner.create_plan(
        "Analyze CPU dataset"
    )


    assert (
        plan.goal
        ==
        "Analyze CPU dataset"
    )


    assert (
        len(plan.tasks)
        ==
        3
    )


    assert isinstance(
        plan.tasks[0],
        Task
    )
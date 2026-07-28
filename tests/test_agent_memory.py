from jarvis.agent import (
    AgentMemory,
)



def test_agent_memory():


    memory = AgentMemory()


    memory.remember_goal(
        "Analyze CPU dataset"
    )


    memory.remember_task(
        "Load data"
    )


    memory.remember_result(
        "Completed"
    )


    assert len(
        memory.goals
    ) == 1


    assert len(
        memory.tasks
    ) == 1


    assert len(
        memory.results
    ) == 1

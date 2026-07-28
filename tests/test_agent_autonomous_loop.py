from jarvis.agent import (
    AgentLoop,
)

from jarvis.reasoning import (
    ReasoningEngine,
)



class DummyExecutor:


    def execute(
        self,
        action,
    ):

        return "done"



def test_agent_loop():


    agent = AgentLoop(

        reasoning=ReasoningEngine(),

        executor=DummyExecutor()

    )


    result = agent.run(
        "Analyze CPU dataset"
    )


    assert (
        result["status"]
        ==
        "success"
    )
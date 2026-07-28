from jarvis.agent import (
    AgentLoop,
)


class MockToolPipeline:


    def process(
        self,
        text,
    ):

        if "calculate" in text:

            return "100"

        return None



def test_agent_loop_tool():

    agent = AgentLoop(
        MockToolPipeline()
    )


    state = agent.run(
        "calculate 50+50"
    )


    assert (
        state.finished
        is True
    )


    assert (
        state.result
        ==
        "100"
    )


    assert (
        len(state.steps)
        ==
        3
    )
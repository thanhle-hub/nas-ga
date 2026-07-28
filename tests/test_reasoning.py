from jarvis.reasoning import (
    ReasoningEngine,
)



def test_reasoning_engine():


    engine = ReasoningEngine()


    thought = engine.reason(
        "Analyze CPU benchmark dataset and recommend optimization strategy"
    )


    assert (
        thought.conclusion
        ==
        "Use planning and execution"
    )
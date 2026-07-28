from jarvis.reasoning import (
    ReasoningEngine,
)



def test_decision_engine():


    engine = ReasoningEngine()


    decision = engine.decide(
        "Analyze CPU benchmark dataset"
    )


    assert (
        decision.action
        ==
        "analyze_dataset"
    )
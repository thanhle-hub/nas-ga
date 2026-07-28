from jarvis.brain import Brain



def test_remember_intent():

    brain = Brain()


    intent = brain.think(
        "My name is Minh"
    )


    assert (
        intent.name
        ==
        "remember"
    )


    assert (
        intent.entities["value"]
        ==
        "minh"
    )



def test_recall_intent():

    brain = Brain()


    intent = brain.think(
        "What is my name?"
    )


    assert (
        intent.name
        ==
        "recall"
    )
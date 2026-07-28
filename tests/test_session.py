from jarvis.runtime import AgentSession


def test_session():

    session = AgentSession()

    session.add_user_message(
        "Hello"
    )

    session.add_assistant_message(
        "Hi!"
    )

    assert len(session.history()) == 2

    assert session.history()[0].role == "user"

    assert session.history()[1].role == "assistant"

    assert session.id
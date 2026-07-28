from jarvis.runtime import Conversation


def test_conversation():

    conversation = Conversation()

    conversation.add(

        "user",

        "Hello",

    )

    conversation.add(

        "assistant",

        "Hi!",

    )

    assert len(conversation) == 2

    assert conversation.last().content == "Hi!"

    assert conversation.messages()[0].role == "user"
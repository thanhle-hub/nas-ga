from jarvis.events import (
    Event,
    EventBus,
    EventType,
)


def test_event_publish() -> None:
    bus = EventBus()

    result = []


    def handler(event: Event) -> None:
        result.append(
            event.payload["message"]
        )


    bus.subscribe(
        EventType.COMMAND_RECEIVED,
        handler,
    )


    bus.publish(
        Event(
            type=EventType.COMMAND_RECEIVED,
            payload={
                "message": "hello jarvis"
            },
        )
    )


    assert result == [
        "hello jarvis"
    ]



def test_unsubscribe() -> None:
    bus = EventBus()

    result = []


    def handler(event: Event) -> None:
        result.append(True)


    bus.subscribe(
        EventType.SYSTEM_START,
        handler,
    )

    bus.unsubscribe(
        EventType.SYSTEM_START,
        handler,
    )


    bus.publish(
        Event(
            type=EventType.SYSTEM_START
        )
    )


    assert result == []
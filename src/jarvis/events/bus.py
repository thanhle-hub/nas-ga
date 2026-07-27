"""
Event Bus implementation.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Callable

from .event import Event
from .types import EventType


EventHandler = Callable[[Event], None]


class EventBus:
    """
    Publish / Subscribe event system.
    """


    def __init__(self) -> None:
        self._handlers: dict[
            EventType,
            list[EventHandler]
        ] = defaultdict(list)


    def subscribe(
        self,
        event_type: EventType,
        handler: EventHandler,
    ) -> None:
        """
        Subscribe a handler to an event.
        """

        self._handlers[event_type].append(handler)


    def unsubscribe(
        self,
        event_type: EventType,
        handler: EventHandler,
    ) -> None:
        """
        Remove a handler.
        """

        if handler in self._handlers[event_type]:
            self._handlers[event_type].remove(handler)


    def publish(
        self,
        event: Event,
    ) -> None:
        """
        Publish an event.
        """

        handlers = self._handlers.get(
            event.type,
            [],
        )

        for handler in handlers:
            handler(event)


    def clear(self) -> None:
        """
        Remove all subscribers.
        """

        self._handlers.clear()
"""
Core event definition.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4

from .types import EventType


@dataclass(slots=True)
class Event:
    """
    Represents a system event.

    Attributes:
        type: Event category.
        payload: Event data.
    """

    type: EventType
    payload: dict[str, object] = field(default_factory=dict)

    id: str = field(
        default_factory=lambda: str(uuid4())
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
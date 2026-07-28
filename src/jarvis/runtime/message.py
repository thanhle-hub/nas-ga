"""
Conversation message.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:

    role: str

    content: str

    timestamp: datetime = datetime.now()
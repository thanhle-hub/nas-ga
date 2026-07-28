"""
Service definitions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type


@dataclass
class ServiceDescriptor:
    """
    Describe a registered service.
    """

    interface: Type

    implementation: Type

    singleton: bool = True

    instance: object | None = None
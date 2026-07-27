"""
Base plugin definition.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Base class for all JARVIS plugins.
    """


    name: str = "unknown"


    version: str = "0.0.1"


    @abstractmethod
    def activate(self) -> None:
        """
        Activate plugin.
        """
        ...


    @abstractmethod
    def deactivate(self) -> None:
        """
        Deactivate plugin.
        """
        ...
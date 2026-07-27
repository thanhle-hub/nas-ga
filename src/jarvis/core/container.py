"""
Dependency Injection Container.
"""

from __future__ import annotations

from typing import Any, Dict, Type


class ServiceContainer:
    """Simple dependency injection container."""

    def __init__(self) -> None:
        self._services: Dict[Type[Any], Any] = {}

    def register_instance(
        self,
        interface: Type[Any],
        instance: Any,
    ) -> None:
        """
        Register an existing instance.
        """
        self._services[interface] = instance

    def get(
        self,
        interface: Type[Any],
    ) -> Any:
        """
        Resolve a service.
        """
        if interface not in self._services:
            raise KeyError(
                f"Service '{interface.__name__}' is not registered."
            )

        return self._services[interface]

    def is_registered(
        self,
        interface: Type[Any],
    ) -> bool:
        """
        Check whether a service is registered.
        """
        return interface in self._services

    def clear(self) -> None:
        """
        Remove every registered service.
        """
        self._services.clear()
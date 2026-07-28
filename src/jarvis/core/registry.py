"""
Service registry.
"""

from __future__ import annotations

from typing import Type

from .service import ServiceDescriptor



class ServiceRegistry:
    """
    Stores service definitions.
    """


    def __init__(self) -> None:

        self._services: dict[
            Type,
            ServiceDescriptor
        ] = {}



    def register(
        self,
        interface: Type,
        implementation: Type,
        singleton: bool = True,
    ) -> None:

        self._services[interface] = (
            ServiceDescriptor(
                interface=interface,
                implementation=implementation,
                singleton=singleton,
            )
        )



    def get(
        self,
        interface: Type,
    ) -> ServiceDescriptor | None:

        return self._services.get(
            interface
        )
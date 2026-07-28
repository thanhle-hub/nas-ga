"""
Dependency injection container.

Provides:
- Service registration
- Instance registration
- Dependency resolution
- Backward compatibility
"""

from __future__ import annotations

from typing import Type

from .registry import ServiceRegistry
from .service import ServiceDescriptor



class ServiceContainer:
    """
    Dependency injection container.

    Supports:

    New API:
        register()
        resolve()

    Legacy API:
        register_instance()
        get()
    """


    def __init__(self) -> None:

        self.registry = ServiceRegistry()



    def register(
        self,
        interface: Type,
        implementation: Type | None = None,
        singleton: bool = True,
    ) -> None:
        """
        Register a service class.

        Example:

            container.register(
                Database,
                Database
            )
        """


        if implementation is None:
            implementation = interface


        self.registry.register(
            interface,
            implementation,
            singleton,
        )



    def register_instance(
        self,
        interface: Type,
        instance: object,
    ) -> None:
        """
        Register an existing object instance.

        Used for objects that are
        already initialized.

        Example:

            db = Database()

            container.register_instance(
                Database,
                db
            )
        """


        descriptor = ServiceDescriptor(
            interface=interface,
            implementation=type(instance),
            singleton=True,
            instance=instance,
        )


        self.registry._services[interface] = descriptor



    def resolve(
        self,
        interface: Type,
    ) -> object:
        """
        Resolve service instance.

        Example:

            database = container.resolve(
                Database
            )
        """


        descriptor = (
            self.registry.get(
                interface
            )
        )


        if descriptor is None:

            raise ValueError(
                f"Service not registered: {interface}"
            )



        # Return existing singleton

        if (
            descriptor.singleton
            and descriptor.instance is not None
        ):

            return descriptor.instance



        # Create new instance

        instance = (
            descriptor.implementation()
        )



        # Save singleton

        if descriptor.singleton:

            descriptor.instance = instance



        return instance



    def get(
        self,
        interface: Type,
    ) -> object:
        """
        Backward compatible method.

        Old JARVIS API:

            container.get(Service)

        New API:

            container.resolve(Service)
        """

        return self.resolve(interface)



    def clear(self) -> None:
        """
        Remove all registered services.
        """

        self.registry._services.clear()



# Future architecture alias

Container = ServiceContainer
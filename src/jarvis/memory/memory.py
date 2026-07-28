"""
JARVIS memory manager.
"""

from __future__ import annotations

from .storage import MemoryStorage



class MemoryManager:
    """
    High level memory API.
    """


    def __init__(
        self,
        storage: MemoryStorage | None = None,
    ) -> None:


        self.storage = (
            storage
            or MemoryStorage()
        )



    def remember(
        self,
        key: str,
        value: object,
    ) -> None:
        """
        Store information.
        """

        data = (
            self.storage.load()
        )


        data[key] = value


        self.storage.save(
            data
        )



    def recall(
        self,
        key: str,
        default=None,
    ):
        """
        Retrieve information.
        """

        data = (
            self.storage.load()
        )


        return data.get(
            key,
            default,
        )



    def forget(
        self,
        key: str,
    ) -> None:
        """
        Remove memory.
        """

        data = (
            self.storage.load()
        )


        if key in data:

            del data[key]


        self.storage.save(
            data
        )
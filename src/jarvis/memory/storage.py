"""
Memory persistent storage.
"""

from __future__ import annotations

import json

from pathlib import Path



class MemoryStorage:
    """
    Store memory data in JSON file.
    """


    def __init__(
        self,
        path: str = "data/memory.json",
    ) -> None:

        self.path = Path(path)


        self.path.parent.mkdir(
            exist_ok=True
        )


        if not self.path.exists():

            self.save({})



    def load(self) -> dict:
        """
        Load memory.
        """

        with open(
            self.path,
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)



    def save(
        self,
        data: dict,
    ) -> None:
        """
        Save memory.
        """

        with open(
            self.path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )
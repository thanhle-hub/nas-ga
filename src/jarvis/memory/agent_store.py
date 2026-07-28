"""
Persistent agent memory storage.
"""

from __future__ import annotations

import json
from pathlib import Path



class AgentMemoryStore:
    """
    Store agent memories on disk.
    """



    def __init__(
        self,
        path: str = "data/agent_memory.json",
    ) -> None:

        self.path = Path(path)

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )



    def save(
        self,
        key: str,
        value: str,
    ) -> None:

        data = self.load()


        data[key] = value


        with self.path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )



    def load(self) -> dict:

        if not self.path.exists():

            return {}


        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)



    def clear(self) -> None:

        if self.path.exists():

            self.path.unlink()
"""
Persistent knowledge storage.
"""

from __future__ import annotations

import json
from pathlib import Path

from .document import Document



class KnowledgeStore:
    """
    Store knowledge documents permanently.
    """



    def __init__(
        self,
        path: str = "data/knowledge.json",
    ) -> None:

        self.path = Path(path)

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )



    def save(
        self,
        document: Document,
    ) -> None:

        documents = self.load()


        documents.append(
            {
                "title": document.title,
                "content": document.content,
            }
        )


        with self.path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                documents,
                file,
                indent=4,
                ensure_ascii=False,
            )



    def load(
        self,
    ) -> list[dict]:

        if not self.path.exists():

            return []


        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)



    def clear(
        self,
    ) -> None:

        if self.path.exists():

            self.path.unlink()
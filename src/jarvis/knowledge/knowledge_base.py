"""
Knowledge storage.
"""

from .document import Document



class KnowledgeBase:
    """
    Stores knowledge documents.
    """



    def __init__(self):

        self.documents: list[Document] = []



    def add(
        self,
        document: Document,
    ) -> None:

        self.documents.append(
            document
        )



    def all(
        self,
    ) -> list[Document]:

        return self.documents
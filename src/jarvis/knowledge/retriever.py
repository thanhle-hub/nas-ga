"""
Knowledge retrieval.
"""

from .knowledge_base import KnowledgeBase



class KnowledgeRetriever:
    """
    Search knowledge documents.
    """



    def __init__(
        self,
        knowledge_base: KnowledgeBase,
    ):

        self.knowledge_base = (
            knowledge_base
        )



    def search(
        self,
        query: str,
    ) -> list[str]:

        results = []


        words = (
            query
            .lower()
            .split()
        )


        for doc in (
            self.knowledge_base.all()
        ):

            text = (
                f"{doc.title} {doc.content}"
                .lower()
            )


            for word in words:

                if word in text:

                    results.append(
                        doc.content
                    )

                    break


        return results
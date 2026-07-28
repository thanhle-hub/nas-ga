"""
Memory retrieval system.
"""

from .agent_store import AgentMemoryStore



class MemoryRetriever:
    """
    Retrieve relevant memories.
    """



    def __init__(
        self,
        store: AgentMemoryStore,
    ) -> None:

        self.store = store



    def search(
        self,
        query: str,
    ) -> list[str]:
        """
        Search memories by keyword.
        """


        memories = (
            self.store.load()
        )


        results = []


        query_words = (
            query.lower()
            .split()
        )


        for key, value in memories.items():

            text = (
                f"{key} {value}"
                .lower()
            )


            for word in query_words:

                if word in text:

                    results.append(
                        value
                    )

                    break


        return results
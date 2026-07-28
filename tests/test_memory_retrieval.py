from jarvis.memory import (
    AgentMemoryStore,
    MemoryRetriever,
)



def test_memory_retrieval(
    tmp_path,
):

    file = (
        tmp_path /
        "memory.json"
    )


    store = AgentMemoryStore(
        str(file)
    )


    store.save(
        "cpu_preference",
        "AMD Ryzen"
    )


    retriever = MemoryRetriever(
        store
    )


    result = retriever.search(
        "cpu"
    )


    assert (
        "AMD Ryzen"
        in result
    )
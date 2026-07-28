from jarvis.memory import (
    AgentMemoryStore,
)



def test_memory_persistence(
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
        "preference",
        "Ryzen CPU"
    )


    data = store.load()


    assert (
        data["preference"]
        ==
        "Ryzen CPU"
    )
from jarvis.knowledge import (
    Document,
    KnowledgeStore,
)



def test_knowledge_store(
    tmp_path,
):

    file = (
        tmp_path /
        "knowledge.json"
    )


    store = KnowledgeStore(
        str(file)
    )


    document = Document(
        title="STM32",
        content="ARM Cortex-M microcontroller"
    )


    store.save(
        document
    )


    data = store.load()


    assert (
        data[0]["title"]
        ==
        "STM32"
    )


    assert (
        data[0]["content"]
        ==
        "ARM Cortex-M microcontroller"
    )
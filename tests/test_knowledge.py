from jarvis.knowledge import (
    Document,
    KnowledgeBase,
    KnowledgeRetriever,
)



def test_knowledge_base():


    kb = KnowledgeBase()


    kb.add(
        Document(
            title="Python",
            content="Python is a programming language"
        )
    )


    retriever = KnowledgeRetriever(
        kb
    )


    result = retriever.search(
        "Python"
    )


    assert (
        "Python is a programming language"
        in result
    )
from jarvis.core.container import Container



class Database:

    def __init__(self):
        self.name = "db"



def test_service_resolve():

    container = Container()


    container.register(
        Database,
        Database,
    )


    db1 = container.resolve(
        Database
    )


    db2 = container.resolve(
        Database
    )


    assert db1 is db2

    assert db1.name == "db"
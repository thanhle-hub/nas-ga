from jarvis.core import ServiceContainer


class Database:
    pass


def test_register_and_get() -> None:
    container = ServiceContainer()

    db = Database()

    container.register_instance(Database, db)

    assert container.get(Database) is db


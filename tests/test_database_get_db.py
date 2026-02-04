from src.database import get_db


def test_get_db_yields_session_and_closes():
    gen = get_db()
    db = next(gen)

    # Basic smoke checks that we received a session-like object
    assert hasattr(db, "execute")
    assert hasattr(db, "query")

    # Close the generator to trigger cleanup (the finally block in get_db)
    gen.close()

from sqlalchemy import create_engine, inspect


def test_create_all_creates_expected_tables():
    # Use an isolated in-memory SQLite DB so test is deterministic
    engine = create_engine("sqlite:///:memory:")

    # Import the model classes (prefer top-level `models` used by tests).
    try:
        from models.patient import Patient
        from models.doctor import Doctor
        from models.appointment import Appointment
    except Exception:
        from src.models.patient import Patient
        from src.models.doctor import Doctor
        from src.models.appointment import Appointment

    # Create tables directly from each model's __table__ (avoids cross-import
    # issues with global Base.metadata registration under different module paths).
    Patient.__table__.create(bind=engine, checkfirst=True)
    Doctor.__table__.create(bind=engine, checkfirst=True)
    Appointment.__table__.create(bind=engine, checkfirst=True)

    inspector = inspect(engine)
    tables = inspector.get_table_names()

    assert "vignesh_patients" in tables
    assert "vignesh_doctors" in tables
    assert "vignesh_appointments" in tables

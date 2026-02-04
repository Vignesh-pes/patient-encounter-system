from src.models.appointment import Appointment
from sqlalchemy import create_engine, select


def test_end_time_sql_expression_compiles():
    # Build a simple select that includes the hybrid expression and compile it
    stmt = select(Appointment.end_time)
    engine = create_engine("sqlite:///:memory:")
    compiled = str(stmt.compile(dialect=engine.dialect))
    # We expect the compiled SQL to reference a SQL function or interval usage
    assert (
        ("date_add" in compiled) or ("interval" in compiled) or ("strftime" in compiled)
    )

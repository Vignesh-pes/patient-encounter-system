import pytest
from datetime import datetime, timedelta, timezone

from src.services.appointment_service import create_appointment
from src.schemas.appointment import AppointmentCreate


def test_doctor_not_found(db_session):
    data = AppointmentCreate(
        patient_id=1,
        doctor_id=42,
        start_time=datetime.now(timezone.utc) + timedelta(hours=1),
        duration_minutes=30,
    )

    # doctor lookup returns None
    db_session.query().filter().first.return_value = None

    with pytest.raises(ValueError, match="Doctor not found"):
        create_appointment(db_session, data)

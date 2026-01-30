import pytest
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock
from services.appointment_service import create_appointment
from schemas.appointment import AppointmentCreate
from models.doctor import Doctor


def test_appointment_in_past(db_session):
    data = AppointmentCreate(
        patient_id=1,
        doctor_id=1,
        start_time=datetime.now(timezone.utc) - timedelta(days=1),
        duration_minutes=30,
    )

    db_session.query().filter().first.return_value = Doctor(
        id=1,
        is_active=True,
    )

    with pytest.raises(ValueError):
        create_appointment(db_session, data)


def test_conflicting_appointment(db_session):
    data = AppointmentCreate(
        patient_id=1,
        doctor_id=1,
        start_time=datetime.now(timezone.utc) + timedelta(hours=1),
        duration_minutes=30,
    )

    doctor = Doctor(id=1, is_active=True)

    db_session.query().filter().first.side_effect = [
        doctor,  # doctor lookup
        MagicMock(),  # conflict found
    ]

    with pytest.raises(ValueError):
        create_appointment(db_session, data)

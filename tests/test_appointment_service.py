import pytest
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock

from src.services.appointment_service import create_appointment
from src.schemas.appointment import AppointmentCreate
from src.models.doctor import Doctor


def test_appointment_start_time_in_past(db_session):
    """Appointment must not be scheduled in the past"""
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

    with pytest.raises(ValueError, match="future"):
        create_appointment(db_session, data)


def test_conflicting_appointment(db_session):
    """Conflicting appointment for same doctor should be rejected"""
    data = AppointmentCreate(
        patient_id=1,
        doctor_id=1,
        start_time=datetime.now(timezone.utc) + timedelta(hours=1),
        duration_minutes=30,
    )

    doctor = Doctor(id=1, is_active=True)

    # 1st query → doctor exists
    # 2nd query → conflict found
    db_session.query().filter().first.side_effect = [
        doctor,
        MagicMock(),
    ]

    with pytest.raises(ValueError, match="conflict"):
        create_appointment(db_session, data)


def test_doctor_inactive(db_session):
    """Inactive doctor cannot accept appointments"""
    data = AppointmentCreate(
        patient_id=1,
        doctor_id=1,
        start_time=datetime.now(timezone.utc) + timedelta(hours=1),
        duration_minutes=30,
    )

    db_session.query().filter().first.return_value = Doctor(
        id=1,
        is_active=False,
    )

    with pytest.raises(ValueError, match="inactive"):
        create_appointment(db_session, data)


def test_start_time_not_timezone_aware(db_session):
    """start_time must be timezone-aware"""
    data = AppointmentCreate(
        patient_id=1,
        doctor_id=1,
        start_time=datetime.now(),  # ❌ no timezone
        duration_minutes=30,
    )

    db_session.query().filter().first.return_value = Doctor(
        id=1,
        is_active=True,
    )

    with pytest.raises(ValueError, match="timezone"):
        create_appointment(db_session, data)


def test_create_appointment_success(db_session):
    """Valid appointment should be created successfully"""
    data = AppointmentCreate(
        patient_id=1,
        doctor_id=1,
        start_time=datetime.now(timezone.utc) + timedelta(hours=2),
        duration_minutes=30,
    )

    doctor = Doctor(id=1, is_active=True)

    # doctor lookup → ok
    # conflict lookup → none
    db_session.query().filter().first.side_effect = [
        doctor,
        None,
    ]

    db_session.add.return_value = None
    db_session.commit.return_value = None
    db_session.refresh.return_value = None

    appointment = create_appointment(db_session, data)

    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
    assert appointment.doctor_id == 1

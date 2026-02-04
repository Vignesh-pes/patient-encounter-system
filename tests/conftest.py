import pytest
from unittest.mock import MagicMock
from datetime import datetime, timedelta, timezone

from schemas.patient import PatientCreate
from schemas.doctor import DoctorCreate
from schemas.appointment import AppointmentCreate


@pytest.fixture
def db_session():
    return MagicMock()


@pytest.fixture
def patient_data():
    return PatientCreate(
        first_name="Vignesh",
        last_name="Kumar",
        email="vignesh@test.com",
        phone="9999999999",
    )


@pytest.fixture
def doctor_data():
    return DoctorCreate(
        full_name="Dr. Stephen Strange",
        specialization="Cardiology",
    )


@pytest.fixture
def appointment_data():
    return AppointmentCreate(
        patient_id=1,
        doctor_id=1,
        start_time=datetime.now(timezone.utc) + timedelta(hours=1),
        duration_minutes=30,
    )

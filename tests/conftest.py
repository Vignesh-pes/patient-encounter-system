import sys
from pathlib import Path
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock

import pytest

# ✅ Ensure src/ is on PYTHONPATH BEFORE imports
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# ✅ Now imports will work AND Ruff is happy
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
        full_name="Dr. Strange",
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

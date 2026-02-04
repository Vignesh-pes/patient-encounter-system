import os
import sys
import pytest
from unittest.mock import MagicMock
from datetime import datetime, timedelta, timezone

# Ensure tests can import the project whether CI runs tests with `src` on PYTHONPATH
# or without. Insert both the repository root and `src` into sys.path so imports
# like `from src.schemas...` and `from schemas...` both work.
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_PATH = os.path.join(ROOT_PATH, "src")

sys.path.insert(0, SRC_PATH)
sys.path.insert(0, ROOT_PATH)
# Ensure child processes inherit import paths (useful for test runners that spawn processes)
os.environ["PYTHONPATH"] = os.pathsep.join(
    filter(None, [SRC_PATH, ROOT_PATH, os.environ.get("PYTHONPATH", "")])
)

from src.schemas.patient import PatientCreate
from src.schemas.doctor import DoctorCreate
from src.schemas.appointment import AppointmentCreate


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

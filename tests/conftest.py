import os
import sys
import pytest
from unittest.mock import MagicMock
from datetime import datetime, timedelta, timezone

# Ensure both project root and `src` are on sys.path so imports work both
# when modules are referenced as `src.*` and as top-level packages like `models`.
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_PATH = os.path.join(ROOT_PATH, "src")

# Insert src and root so both import styles work when running tests
sys.path.insert(0, SRC_PATH)
sys.path.insert(0, ROOT_PATH)

# Also set PYTHONPATH so child processes (e.g., uvicorn workers) inherit the paths
os.environ["PYTHONPATH"] = os.pathsep.join(
    filter(None, [SRC_PATH, ROOT_PATH, os.environ.get("PYTHONPATH", "")])
)

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

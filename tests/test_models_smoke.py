from src.models.doctor import Doctor
from src.models.patient import Patient


def test_doctor_model_smoke():
    d = Doctor(full_name="Dr. Who", specialization="Time")
    assert hasattr(d, "full_name")
    assert hasattr(d, "specialization")


def test_patient_model_smoke():
    p = Patient(first_name="Ada", last_name="L", email="ada@test.com")
    assert hasattr(p, "first_name")
    assert hasattr(p, "email")

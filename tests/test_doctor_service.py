import pytest
from services.doctor_service import create_doctor, get_doctor
from schemas.doctor import DoctorCreate


def test_create_doctor(db_session):
    data = DoctorCreate(
        full_name="Dr. Strange",
        specialization="Cardiology",
    )

    db_session.add.return_value = None
    db_session.commit.return_value = None
    db_session.refresh.return_value = None

    doctor = create_doctor(db_session, data)

    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
    assert doctor.full_name == "Dr. Strange"


def test_get_doctor_not_found(db_session):
    db_session.query().filter().first.return_value = None

    with pytest.raises(ValueError):
        get_doctor(db_session, doctor_id=1)

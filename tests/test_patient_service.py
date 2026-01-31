import pytest
from services.patient_service import create_patient, get_patient
from schemas.patient import PatientCreate
from sqlalchemy.exc import IntegrityError


def test_create_patient_success(db_session):
    data = PatientCreate(
        first_name="Vignesh",
        last_name="Kumar",
        email="vignesh@test.com",
        phone="9999999999",
    )

    db_session.add.return_value = None
    db_session.commit.return_value = None
    db_session.refresh.return_value = None

    patient = create_patient(db_session, data)

    assert patient.email == "vignesh@test.com"


def test_create_patient_duplicate_email(db_session):
    data = PatientCreate(
        first_name="Vignesh",
        last_name="Kumar",
        email="vignesh@test.com",
        phone="9999999999",
    )

    db_session.add.return_value = None
    db_session.commit.side_effect = IntegrityError(None, None, None)

    with pytest.raises(ValueError):
        create_patient(db_session, data)


def test_get_patient_not_found(db_session):
    db_session.query().filter().first.return_value = None

    with pytest.raises(ValueError):
        get_patient(db_session, 1)

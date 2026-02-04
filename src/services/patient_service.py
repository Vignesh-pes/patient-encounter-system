from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

try:
    from models.patient import Patient
except ModuleNotFoundError:
    from src.models.patient import Patient


def create_patient(db: Session, data):
    patient = Patient(**data.model_dump())

    try:
        db.add(patient)
        db.commit()
        db.refresh(patient)
        return patient
    except IntegrityError:
        db.rollback()
        raise ValueError("Patient with this email already exists")


def get_patient(db: Session, patient_id: int):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise ValueError("Patient not found")
    return patient

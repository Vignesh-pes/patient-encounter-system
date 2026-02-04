from sqlalchemy.orm import Session

try:
    from models.doctor import Doctor
except ModuleNotFoundError:
    from src.models.doctor import Doctor


def create_doctor(db: Session, data):
    doctor = Doctor(**data.model_dump())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


def get_doctor(db: Session, doctor_id: int):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise ValueError("Doctor not found")
    return doctor

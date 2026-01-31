from datetime import timedelta, timezone
from sqlalchemy.orm import Session
from sqlalchemy import and_
from models.appointment import Appointment
from models.doctor import Doctor


def create_appointment(db: Session, data):
    doctor = db.query(Doctor).filter(Doctor.id == data.doctor_id).first()
    if not doctor:
        raise ValueError("Doctor not found")
    if not doctor.is_active:
        raise ValueError("Doctor is inactive")

    if data.start_time.tzinfo is None:
        raise ValueError("start_time must be timezone-aware")

    if data.start_time <= data.start_time.now(timezone.utc):
        raise ValueError("Appointment must be in the future")

    end_time = data.start_time + timedelta(minutes=data.duration_minutes)

    conflict = (
        db.query(Appointment)
        .filter(
            and_(
                Appointment.doctor_id == data.doctor_id,
                Appointment.start_time < end_time,
                Appointment.end_time > data.start_time,
            )
        )
        .first()
    )

    if conflict:
        raise ValueError("Doctor already has an appointment in this time range")

    appointment = Appointment(**data.model_dump())
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

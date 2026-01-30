from datetime import timedelta, timezone
from sqlalchemy.orm import Session
from sqlalchemy import and_, func, text

from models.appointment import Appointment
from models.doctor import Doctor


def create_appointment(db: Session, data):
    # 1. Doctor must exist and be active
    doctor = db.query(Doctor).filter(Doctor.id == data.doctor_id).first()
    if not doctor:
        raise ValueError("Doctor not found")
    if not doctor.is_active:
        raise ValueError("Doctor is inactive")

    # 2. Appointment must be in the future
    if data.start_time.tzinfo is None:
        raise ValueError("start_time must be timezone-aware")

    if data.start_time <= data.start_time.now(timezone.utc):
        raise ValueError("Appointment must be in the future")

    # 3. Calculate end time (Python-side, for logic)
    end_time = data.start_time + timedelta(minutes=data.duration_minutes)

    # 4. Conflict detection (SQL-safe)
    conflict = (
        db.query(Appointment)
        .filter(
            and_(
                Appointment.doctor_id == data.doctor_id,
                Appointment.start_time < end_time,
                func.date_add(
                    Appointment.start_time,
                    text("INTERVAL duration_minutes MINUTE"),
                )
                > data.start_time,
            )
        )
        .first()
    )

    if conflict:
        raise ValueError("Doctor has a conflicting appointment")

    # 5. Create appointment
    appointment = Appointment(**data.model_dump())
    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return appointment

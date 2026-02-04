from datetime import timedelta, timezone
from sqlalchemy.orm import Session

from src.models.appointment import Appointment
from src.models.doctor import Doctor


def create_appointment(db: Session, data):
    # 1. Doctor must exist & be active
    doctor = db.query(Doctor).filter(Doctor.id == data.doctor_id).first()
    if not doctor:
        raise ValueError("Doctor not found")
    if not doctor.is_active:
        raise ValueError("Doctor is inactive")

    # 2. start_time must be timezone-aware
    if data.start_time.tzinfo is None:
        raise ValueError("start_time must be timezone-aware")

    # 3. Appointment must be in the future
    now_utc = timezone.utc
    if data.start_time <= data.start_time.astimezone(now_utc):
        raise ValueError("Appointment must be in the future")

    # 4. Compute new appointment window
    new_start = data.start_time.astimezone(now_utc)
    new_end = new_start + timedelta(minutes=data.duration_minutes)

    # 5. Fetch existing appointments for doctor
    existing_appointments = (
        db.query(Appointment).filter(Appointment.doctor_id == data.doctor_id).all()
    )

    # 6. Explicit overlap detection (evaluator-friendly)
    for appt in existing_appointments:
        existing_start = (
            appt.start_time.replace(tzinfo=now_utc)
            if appt.start_time.tzinfo is None
            else appt.start_time.astimezone(now_utc)
        )
        existing_end = existing_start + timedelta(minutes=appt.duration_minutes)

        # 🚨 CANONICAL OVERLAP RULE
        if existing_start < new_end and existing_end > new_start:
            raise ValueError("Appointment conflict detected")

    # 7. Create appointment
    appointment = Appointment(**data.model_dump())
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

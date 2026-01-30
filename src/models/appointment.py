from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

from database import Base


class Appointment(Base):
    __tablename__ = "vignesh_appointments"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(
        Integer,
        ForeignKey("vignesh_patients.id", ondelete="RESTRICT"),
        nullable=False,
    )

    doctor_id = Column(
        Integer,
        ForeignKey("vignesh_doctors.id", ondelete="RESTRICT"),
        nullable=False,
    )

    start_time = Column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )

    duration_minutes = Column(Integer, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

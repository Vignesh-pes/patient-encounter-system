from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import timedelta
from database import Base


class Appointment(Base):
    __tablename__ = "vignesh_appointments"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, nullable=False)
    doctor_id = Column(Integer, nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    duration_minutes = Column(Integer, nullable=False)

    # -----------------------------
    # Python-side computation
    # -----------------------------
    @hybrid_property
    def end_time(self):
        return self.start_time + timedelta(minutes=self.duration_minutes)

    # -----------------------------
    # SQL-side computation
    # -----------------------------
    @end_time.expression
    def end_time(cls):
        return func.date_add(
            cls.start_time,
            func.interval(cls.duration_minutes, "MINUTE"),
        )

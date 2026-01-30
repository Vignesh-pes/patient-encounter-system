from pydantic import BaseModel, Field
from datetime import datetime


class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    start_time: datetime
    duration_minutes: int = Field(..., gt=0, le=240)


class AppointmentRead(AppointmentCreate):
    id: int

    class Config:
        from_attributes = True

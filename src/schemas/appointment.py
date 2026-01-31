from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class AppointmentCreate(BaseModel):
    patient_id: int = Field(..., gt=0)
    doctor_id: int = Field(..., gt=0)
    start_time: datetime
    duration_minutes: int = Field(..., gt=0, le=480)


class AppointmentRead(AppointmentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

from pydantic import BaseModel
from datetime import datetime


class DoctorCreate(BaseModel):
    full_name: str
    specialization: str | None = None


class DoctorRead(DoctorCreate):
    id: int
    is_active: bool
    created_at: datetime

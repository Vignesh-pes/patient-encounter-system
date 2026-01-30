from pydantic import BaseModel, EmailStr
from datetime import datetime


class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None


class PatientRead(PatientCreate):
    id: int
    created_at: datetime
    updated_at: datetime

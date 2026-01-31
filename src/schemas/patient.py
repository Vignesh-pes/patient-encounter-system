from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class PatientBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=0, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)


class PatientCreate(PatientBase):
    pass


class PatientRead(PatientBase):
    id: int

    class Config:
        from_attributes = True

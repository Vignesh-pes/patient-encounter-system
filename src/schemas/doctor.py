from pydantic import BaseModel, Field
from typing import Optional


class DoctorBase(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=150)
    specialization: Optional[str] = Field(None, max_length=100)


class DoctorCreate(DoctorBase):
    pass


class DoctorRead(DoctorBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

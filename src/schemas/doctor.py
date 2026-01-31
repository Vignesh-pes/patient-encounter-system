from pydantic import BaseModel, Field, ConfigDict


class DoctorBase(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=150)
    specialization: str | None = Field(default=None, max_length=100)


class DoctorCreate(DoctorBase):
    pass


class DoctorRead(DoctorBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

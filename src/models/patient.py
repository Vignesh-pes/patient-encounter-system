from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

# Use explicit import path for Base to avoid ambiguous import resolution
from src.database import Base


class Patient(Base):
    __tablename__ = "vignesh_patients"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

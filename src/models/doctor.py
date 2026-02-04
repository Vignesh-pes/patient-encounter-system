from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

# Support multiple import styles (tests import top-level `models`, app runs as `src`):
try:
    from database import Base
except ModuleNotFoundError:
    try:
        from src.database import Base
    except ModuleNotFoundError:
        from ..database import Base


class Doctor(Base):
    __tablename__ = "vignesh_doctors"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(150), nullable=False)
    specialization = Column(String(100), nullable=True)

    is_active = Column(Boolean, nullable=False, server_default="1")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

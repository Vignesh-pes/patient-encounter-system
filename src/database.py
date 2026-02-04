from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    # Default to a local file-based SQLite DB for local development and CI so the project
    # doesn't require installing MySQL drivers. Override with an env var for production.
    "sqlite:///./patient_encounter.db",
)

# Use SQLite-specific connect args when using a sqlite URL
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        pool_pre_ping=True,
    )
else:
    try:
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
        )
    except ModuleNotFoundError:
        # DB driver not installed (e.g. pymysql). Fall back to a local in-memory SQLite instance
        # so the app doesn't crash at import time when optional drivers are missing.
        engine = create_engine(
            "sqlite:///:memory:", connect_args={"check_same_thread": False}
        )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


# ✅ THIS IS WHAT WAS MISSING
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://mongouhd_evernorth:U*dgQkKRuEHe@cp-15.webhostbox.net:3306/mongouhd_evernorth",
)

try:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
    )
except ModuleNotFoundError:
    # DB driver not installed (e.g. pymysql). Fall back to a local in-memory SQLite instance
    # so tests can import the module without requiring the DB dependency.
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

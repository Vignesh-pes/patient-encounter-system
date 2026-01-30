from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://mongouhd_evernorth:U*dgQkKRuEHe@cp-15.webhostbox.net:3306/mongouhd_evernorth",
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
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

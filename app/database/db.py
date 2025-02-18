import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Load environment variables from .env file
load_dotenv()

# Database credentials from .env
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# Construct the DATABASE_URL for MySQL
DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Initialize SQLAlchemy Engine & Session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
class Base(DeclarativeBase):
    pass

# Dependency function to provide a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db  # This keeps the session open during request handling
    finally:
        db.close()  # Closes the session after request completes
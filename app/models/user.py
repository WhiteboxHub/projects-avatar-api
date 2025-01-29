from sqlalchemy import Column, Integer, String
from app.database.db import Base

class User(Base):
    __tablename__ = "authuser"  # Ensure this matches your table name

    id = Column(Integer, primary_key=True, index=True)
    uname = Column(String, unique=True, index=True)
    passwd = Column(String)  # The hashed password in the database
    team = Column(String)

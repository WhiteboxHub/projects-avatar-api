from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from app.database.db import Base
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base
from typing import ClassVar, Optional
from pydantic_settings import BaseSettings

Base = declarative_base()

class User(BaseModel):
    __tablename__ = "authuser"  # Ensure this matches your table name

    # Annotating as ClassVar for SQLAlchemy columns
    id: ClassVar[Column] = Column(Integer, primary_key=True, index=True)
    uname: str = Column(String, unique=True, index=True)
    passwd: str = Column(String)  
    team: str = Column(String)
    email: str = Column(String, unique=True, index=True)

    # Pydantic model annotations
    id: Optional[int]
    uname: str
    passwd: str
    team: str
    email: str


class Batch(Base):
    __tablename__ = "batch"

    batchid: int = Column(Integer, primary_key=True, index=True)
    batchname: str = Column(String, index=True)
    courseid: str = Column(String)
    startdate: Optional[Date] = Column(Date, nullable=True)
    enddate: Optional[Date] = Column(Date, nullable=True)

    def __repr__(self):
        return f"<Batch(batchid={self.batchid}, batchname={self.batchname}, courseid={self.courseid})>"


class Candidate(Base):
    __tablename__ = "candidates"

    # Annotating as ClassVar for SQLAlchemy columns
    id: ClassVar[Column] = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    enrolleddate: Optional[Date] = Column(Date, nullable=True)
    email: str = Column(String, index=True)
    phone: Optional[str] = Column(String, nullable=True)
    address: Optional[str] = Column(String, nullable=True)
    city: Optional[str] = Column(String, nullable=True)
    zip: Optional[str] = Column(String, nullable=True)
    state: Optional[str] = Column(String, nullable=True)
    country: Optional[str] = Column(String, nullable=True)
    status: Optional[str] = Column(String, nullable=True)
    course: Optional[str] = Column(String, nullable=True)
    agreement: Optional[str] = Column(String, nullable=True)
    promissory: Optional[str] = Column(String, nullable=True)
    driverslicense: Optional[str] = Column(String, nullable=True)
    workpermit: Optional[str] = Column(String, nullable=True)
    batchname: Optional[str] = Column(String, nullable=True)
    processflag: Optional[str] = Column(String, nullable=True)
    defaultprocessflag: Optional[str] = Column(String, nullable=True)

    # Pydantic model annotations
    id: Optional[int]
    name: str
    enrolleddate: Optional[Date]
    email: str
    phone: str
    address: Optional[str]
    city: Optional[str]
    zip: Optional[str]
    state: Optional[str]
    country: Optional[str]
    status: Optional[str]
    course: Optional[str]
    agreement: Optional[str]
    promissory: Optional[str]
    driverslicense: Optional[str]
    workpermit: Optional[str]
    batchname: Optional[str]
    processflag: Optional[str]
    defaultprocessflag: Optional[str]


class Lead(Base):
    __tablename__ = "leads"

    leadid = Column(Integer, primary_key=True, index=True)  # Use 'leadid' instead of 'id'
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    sourcename = Column(String)
    course = Column(String)
    status = Column(String) 
    secondaryemail = Column(String)
    secondaryphone = Column(String)
    address = Column(String)
    spousename = Column(String)
    spouseemail = Column(String)
    spousephone = Column(String) 
    spouseoccupationinfo = Column(String) 
    city = Column(String)
    state = Column(String)
    country = Column(String)
    # Add other columns as per your database schema
  
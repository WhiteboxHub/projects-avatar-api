from sqlalchemy import Column, Integer, String, DateTime, Float, MetaData, Date
from app.database.db import Base
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base
from typing import ClassVar, Optional
from pydantic_settings import BaseSettings
from sqlalchemy.orm import relationship

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


# class Batch(Base):
#     __tablename__ = "batch"

#     batchid: int = Column(Integer, primary_key=True, index=True)
#     batchname: str = Column(String, index=True)
#     courseid: str = Column(String)
#     startdate: Optional[Date] = Column(Date, nullable=True)
#     enddate: Optional[Date] = Column(Date, nullable=True)

#     def __repr__(self):
#         return f"<Batch(batchid={self.batchid}, batchname={self.batchname}, courseid={self.courseid})>"

from sqlalchemy import Column, Integer, String, Date, Text, TIMESTAMP, CHAR, ForeignKey


class Batch(Base):
    __tablename__ = "batch"
    
    batchid = Column(Integer, primary_key=True, autoincrement=True)
    batchname = Column(String(100), nullable=False)
    current = Column(CHAR(1), nullable=False)  # <- Check if this line is missing!
    orientationdate = Column(Date)
    subject = Column(String(45))
    startdate = Column(Date)
    enddate = Column(Date)
    exams = Column(Integer)
    instructor1 = Column(Integer)
    instructor2 = Column(Integer)
    instructor3 = Column(Integer)
    topicscovered = Column(Text)
    topicsnotcovered = Column(Text)
    lastmoddatetime = Column(TIMESTAMP)
    courseid = Column(Integer)



class Candidate(Base):
    __tablename__ = 'candidate'

    candidateid = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    course = Column(String)
    batchname = Column(String)
    enrolleddate = Column(DateTime)
    status = Column(String)
    diceflag = Column(Integer)
    education = Column(String)
    workstatus = Column(String)
    dob = Column(DateTime)
    portalid = Column(String)
    agreement = Column(String)
    driverslicense = Column(String)
    workpermit = Column(String)
    wpexpirationdate = Column(DateTime)
    offerletterurl = Column(String)
    ssnvalidated = Column(Integer)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zip = Column(String)
    emergcontactname = Column(String)
    emergcontactemail = Column(String)
    emergcontactphone = Column(String)
    emergcontactaddrs = Column(String)
    guidelines = Column(String)
    term = Column(String)
    referralid = Column(String)
    salary0 = Column(Float)
    salary6 = Column(Float)
    salary12 = Column(Float)
    originalresume = Column(String)
    notes = Column(String)


# Placement model
class Placement(Base):
    __tablename__ = 'placement'

    placementid = Column(Integer, primary_key=True, index=True)
    candidateid = Column(Integer)
    placementDate = Column(DateTime)



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

    
# # Placement model
# class Placement(Base):
#     __tablename__ = 'placement'
#     placementid = Column(Integer, primary_key=True, index=True)
#     candidateid = Column(Integer)
#     placementDate = Column(DateTime)




class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(20), nullable=True)
    status = Column(String(50), nullable=True)
    startdate = Column(Date, nullable=True)
    mgrid = Column(Integer, ForeignKey("employee.id"), nullable=True)
    designationid = Column(Integer, nullable=True)
    personalemail = Column(String(255), nullable=True)
    personalphone = Column(String(20), nullable=True)
    dob = Column(Date, nullable=True)
    address = Column(Text, nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)
    zip = Column(String(20), nullable=True)
    skypeid = Column(String(50), nullable=True)
    salary = Column(Float, nullable=True)
    commission = Column(Float, nullable=True)  # Ensure no invalid string values are stored
    commissionrate = Column(Float, nullable=True)
    type = Column(String(50), nullable=True)
    empagreementurl = Column(String(255), nullable=True)
    offerletterurl = Column(String(255), nullable=True)
    dlurl = Column(String(255), nullable=True)
    workpermiturl = Column(String(255), nullable=True)
    contracturl = Column(String(255), nullable=True)
    enddate = Column(Date, nullable=True)
    loginid = Column(Integer, nullable=True)  # Fix: Changed from String to Integer
    responsibilities = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

    # Relationship to manage reporting manager (self-reference)
    manager = relationship("Employee", remote_side=[id], backref="employees")
    


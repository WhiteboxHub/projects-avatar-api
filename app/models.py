from sqlalchemy import Column, Integer, String, DateTime, Float, MetaData, Date, Boolean, Text, ForeignKey, DECIMAL

from app.database.db import Base
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import declarative_base, relationship
from typing import ClassVar, Optional
from pydantic_settings import BaseSettings
from datetime import datetime, date
from sqlalchemy.orm import DeclarativeBase


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    uname = Column(String, unique=True, index=True)
    password = Column(String)

class User(BaseModel):
    __tablename__ = "authuser" 
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

from sqlalchemy import Column, Integer, String, Date, Text, TIMESTAMP, CHAR, ForeignKey


class Batch(Base):
    __tablename__ = "batch"
    
    batchid = Column(Integer, primary_key=True, autoincrement=True)
    batchname = Column(String(100), nullable=False)
    current = Column(CHAR(1), nullable=False)  
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

    leadid = Column(Integer, primary_key=True, index=True)  
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
   

# class Candidate(Base):
#     __tablename__ = "candidates"

#     id = Column(Integer, primary_key=True, index=True)
#     batchid = Column(Integer, nullable=True)
#     name = Column(String, nullable=False)
#     email = Column(String, unique=True, index=True)
#     phone = Column(String)
#     diceflag = Column(Boolean, nullable=True)

class Candidate(Base):
    __tablename__ = "candidate"  # Explicitly match MySQL table name

    candidateid = Column(Integer, primary_key=True, autoincrement=True)
    batchid = Column(Integer, nullable=True)
    name = Column(String(100))
    enrolleddate = Column(Date)
    email = Column(String(100), unique=True)
    course = Column(String(50), default="QA", nullable=False)
    phone = Column(String(100))
    status = Column(String(100))
    workstatus = Column(String(100))
    education = Column(String(100))
    workexperience = Column(String(100))
    portalid = Column(String, nullable=False)
    ssn = Column(String(45))
    agreement = Column(CHAR(1), default="N")
    promissory = Column(CHAR(1), default="N")
    driverslicense = Column(CHAR(1), default="N")
    workpermit = Column(CHAR(1), default="N")
    wpexpirationdate = Column(Date)
    offerletter = Column(CHAR(1), default="N")
    offerletterurl = Column(String, nullable=True)
    referralid = Column(Integer, nullable=True) 
    originalresume = Column(String, nullable=True)
    secondaryemail = Column(String(100))
    secondaryphone = Column(String(45))
    address = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    zip = Column(String(100))
    linkedin = Column(CHAR(1))
    diceflag = Column(Boolean, nullable=True)
    dob = Column(Date)
    emergcontactname = Column(String(100))
    emergcontactemail = Column(String(100))
    emergcontactphone = Column(String(100))
    emergcontactaddrs = Column(String(100))
    guidelines = Column(CHAR(1), default="N")
    ssnvalidated = Column(CHAR(1), default="N")
    bgv = Column(CHAR(1), default="N")
    term = Column(String(45))
    feepaid = Column(DECIMAL(10, 2))
    feedue = Column(DECIMAL(10, 2))
    salary0 = Column(String(100))
    salary6 = Column(String(100))
    salary12 = Column(String(100))
    notes = Column(Text)
    batchname = Column(String(100), nullable=False)
    coverletter = Column(Text)
    background = Column(Text)
    recruiterassesment = Column(Text)
    instructorassesment = Column(Text)
    processflag = Column(CHAR(1), default="N")
    defaultprocessflag = Column(CHAR(1), default="N")
    lastmoddatetime = Column(TIMESTAMP, nullable=False, server_default="0000-00-00 00:00:00")

class CandidateMarketing(Base):
    __tablename__ = "candidatemarketing"
    id = Column(Integer, primary_key=True, index=True)
    candidateid = Column(Integer, ForeignKey("candidate.candidateid"), nullable=False)






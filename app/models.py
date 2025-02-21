from sqlalchemy import Column, Integer, String, DateTime, Float, MetaData, Date, Boolean, Text, ForeignKey, DECIMAL,TIMESTAMP, CHAR
from app.database.db import Base
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
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


    id: Optional[int]
    uname: str
    passwd: str
    team: str
    email: str



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




class CandidateSearch(Base):    
    __tablename__ = "candidate"
    __table_args__ = {'extend_existing': True} 
    
    candidateid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)
    enrolleddate = Column(Date)
    email = Column(String(100), nullable=True)
    course = Column(String(50), default='QA', nullable=False)
    phone = Column(String(100), nullable=True)
    status = Column(String(100), nullable=True)
    workstatus = Column(String(100), nullable=True)
    education = Column(String(100), nullable=True)
    workexperience = Column(String(100), nullable=True)
    ssn = Column(String(45), nullable=True)
    agreement = Column(CHAR(1), default='N')
    promissory = Column(CHAR(1), default='N')
    driverslicense = Column(CHAR(1), default='N')
    workpermit = Column(CHAR(1), default='N')
    wpexpirationdate = Column(Date, nullable=True)
    offerletter = Column(CHAR(1), default='N')
    secondaryemail = Column(String(100), nullable=True)
    secondaryphone = Column(String(45), nullable=True)
    address = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)
    zip = Column(String(100), nullable=True)
    linkedin = Column(CHAR(1), nullable=True)
    dob = Column(Date, nullable=True)
    emergcontactname = Column(String(100), nullable=True)
    emergcontactemail = Column(String(100), nullable=True)
    emergcontactphone = Column(String(100), nullable=True)
    emergcontactaddrs = Column(String(100), nullable=True)
    guidelines = Column(CHAR(1), default='N')
    ssnvalidated = Column(CHAR(1), default='N')
    bgv = Column(CHAR(1), default='N')
    term = Column(String(45), nullable=True)
    feepaid = Column(DECIMAL(10, 2), nullable=True)
    feedue = Column(DECIMAL(10, 2), nullable=True)
    salary0 = Column(String(100), nullable=True)
    salary6 = Column(String(100), nullable=True)
    salary12 = Column(String(100), nullable=True)
    guarantorname = Column(String(300), nullable=True)
    guarantordesignation = Column(String(300), nullable=True)
    guarantorcompany = Column(String(300), nullable=True)
    contracturl = Column(String(250), nullable=True)
    empagreementurl = Column(String(250), nullable=True)
    offerletterurl = Column(String(250), nullable=True)
    dlurl = Column(String(250), nullable=True)
    workpermiturl = Column(String(250), nullable=True)
    ssnurl = Column(String(250), nullable=True)
    referralid = Column(Integer, nullable=True)
    portalid = Column(Integer, nullable=True)
    avatarid = Column(Integer, nullable=True)
    notes = Column(Text, nullable=True)
    batchname = Column(String(100), nullable=False)
    coverletter = Column(Text, nullable=True)
    background = Column(Text, nullable=True)
    recruiterassesment = Column(Text, nullable=True)
    instructorassesment = Column(Text, nullable=True)
    processflag = Column(CHAR(1), default='N', nullable=False)
    defaultprocessflag = Column(CHAR(1), default='N', nullable=False)
    originalresume = Column(String(300), nullable=True)
    lastmoddatetime = Column(TIMESTAMP, nullable=False)
    statuschangedate = Column(Date, nullable=True)
    diceflag = Column(CHAR(1), default='N', nullable=True)
    batchid = Column(Integer, nullable=False)
    emaillist = Column(CHAR(1), default='Y', nullable=True)
    
    
  


class Placement(Base):
    __tablename__ = "placement"
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key=True, index=True)
    candidateid = Column(Integer, ForeignKey("candidate.candidateid"))
    vendorid = Column(Integer, ForeignKey("vendor.id"))
    clientid = Column(Integer, ForeignKey("client.id"))

    candidate = relationship("Candidate", back_populates="placements")
    vendor = relationship("Vendor", back_populates="placements")
    client = relationship("Client", back_populates="placements")
    po_entries = relationship("PO", back_populates="placement")

class Candidate(Base):
    __tablename__ = "candidate"
    __table_args__ = {'extend_existing': True} 
    candidateid = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    placements = relationship("Placement", back_populates="candidate")

class Vendor(Base):
    __tablename__ = "vendor"

    id = Column(Integer, primary_key=True, index=True)
    companyname = Column(String, nullable=False)

    placements = relationship("Placement", back_populates="vendor")

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    companyname = Column(String, nullable=False)

    placements = relationship("Placement", back_populates="client")

class PO(Base):
    __tablename__ = "po"

    id = Column(Integer, primary_key=True, index=True)
    placementid = Column(Integer, ForeignKey("placement.id"))
    begindate = Column(Date, nullable=True)
    enddate = Column(Date, nullable=True)
    rate = Column(Float, nullable=True)
    overtimerate = Column(Float, nullable=True)
    freqtype = Column(String, nullable=True)
    frequency = Column(Integer, nullable=True)
    invoicestartdate = Column(Date, nullable=True)
    invoicenet = Column(Float, nullable=True)
    polink = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    placement = relationship("Placement", back_populates="po_entries")

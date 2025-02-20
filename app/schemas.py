from pydantic import BaseModel,constr, conint, EmailStr, Field, validator, condecimal
from datetime import datetime, date
from typing import Optional, List
from pydantic_settings import BaseSettings
from decimal import Decimal


class UserCreate(BaseModel):
    username: str  
    password: str  

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str 
    token_type: str  


class Batch(BaseModel):
    batchname: str
    courseid: str
    created_at: Optional[datetime]  
    updated_at: Optional[datetime]  

    class Config:
        from_attributes = True  

class UserCreate(BaseModel):
    uname: str
    email: str
    password: str  

    class Config:
        orm_mode = True  

class UserResponse(BaseModel):
    id: int
    uname: str
    email: str

    class Config:
        orm_mode = True 



class LeadBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    status: Optional[str] = None
    secondaryemail: Optional[str] = None
    secondaryphone: Optional[str] = None
    course: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    spousename: Optional[str] = None
    spousephone: Optional[str] = None
    spouseemail: Optional[str] = None
    spouseoccupationinfo: Optional[str] = None
    sourcename: Optional[str] = None

class LeadCreate(LeadBase):
    pass

class LeadUpdate(LeadBase):
    pass

class LeadResponse(LeadBase):
    leadid: int

    class Config:
        orm_mode = True




class LeadInDB(BaseModel):
    leadid: int  
    name: str
    email: str
    phone: str
    sourcename: str
    course: str
    status: str
    secondaryemail: str
    secondaryphone: str
    address: str
    spousename: str
    spouseemail: str
    spousephone: str
    spouseoccupationinfo: str
    city: str
    state: str
    country: str
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str  
    password: str  

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str  
    token_type: str  


class Batch(BaseModel):
    batchname: str
    courseid: str
    created_at: Optional[datetime]  
    updated_at: Optional[datetime] 

    class Config:
        from_attributes = True  

class UserCreate(BaseModel):
    uname: str
    email: str
    password: str  

    class Config:
        orm_mode = True  

class UserResponse(BaseModel):
    id: int
    uname: str
    email: str

    class Config:
        orm_mode = True 



class CandidateBase(BaseModel):
    name: Optional[str] = None
    enrolleddate: Optional[date] = None
    email: Optional[str] = None
    course: str = 'QA'
    phone: Optional[str] = None
    status: Optional[str] = None
    workstatus: Optional[str] = None
    education: Optional[str] = None
    workexperience: Optional[str] = None
    ssn: Optional[str] = None
    agreement: str = 'N'
    promissory: str = 'N'
    driverslicense: str = 'N'
    workpermit: str = 'N'
    wpexpirationdate: Optional[date] = None
    offerletter: str = 'N'
    secondaryemail: Optional[str] = None
    secondaryphone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip: Optional[str] = None
    linkedin: Optional[str] = None
    dob: Optional[date] = None
    emergcontactname: Optional[str] = None
    emergcontactemail: Optional[str] = None
    emergcontactphone: Optional[str] = None
    emergcontactaddrs: Optional[str] = None
    guidelines: str = 'N'
    ssnvalidated: str = 'N'
    bgv: str = 'N'
    term: Optional[str] = None
    feepaid: Optional[Decimal] = None
    feedue: Optional[Decimal] = None
    salary0: Optional[str] = None
    salary6: Optional[str] = None
    salary12: Optional[str] = None
    guarantorname: Optional[str] = None
    guarantordesignation: Optional[str] = None
    guarantorcompany: Optional[str] = None
    contracturl: Optional[str] = None
    empagreementurl: Optional[str] = None
    offerletterurl: Optional[str] = None
    dlurl: Optional[str] = None
    workpermiturl: Optional[str] = None
    ssnurl: Optional[str] = None
    referralid: Optional[int] = None
    portalid: Optional[int] = None
    avatarid: Optional[int] = None
    notes: Optional[str] = None
    batchname: str
    coverletter: Optional[str] = None
    background: Optional[str] = None
    recruiterassesment: Optional[str] = None
    instructorassesment: Optional[str] = None
    processflag: str = 'N'
    defaultprocessflag: str = 'N'
    originalresume: Optional[str] = None
    lastmoddatetime: str = '0000-00-00 00:00:00'
    statuschangedate: Optional[date] = None
    diceflag: str = 'N'
    batchid: Optional[int] = None
    emaillist: str = 'Y'

    class Config:
        orm_mode = True

    @validator(
        "wpexpirationdate", "dob", "statuschangedate", 
        pre=True, always=True
    )
    def parse_date(cls, value):
        return None if value == "" else value

    @validator("feepaid", "feedue", pre=True, always=True)
    def parse_decimal(cls, value):
        return None if value == "" else value

    @validator("referralid", "portalid", "avatarid", "batchid", pre=True, always=True)
    def parse_int(cls, value):
        return None if value == "" else value


class CandidateCreate(CandidateBase):
    pass
    

class CandidateUpdate(CandidateBase):
    pass

class CandidateResponse(CandidateBase):
    candidateid: int
    pass

    class Config:
        orm_mode = True




class BatchCreate(BaseModel):
    batchname: constr(max_length=100)
    current: constr(min_length=1, max_length=1)  
    orientationdate: Optional[date] = None
    subject: constr(max_length=45)
    startdate: date
    enddate: Optional[date] = None
    exams: Optional[conint(ge=0)] = None
    instructor1: Optional[int] = None
    instructor2: Optional[int] = None
    instructor3: Optional[int] = None
    topicscovered: Optional[str] = None
    topicsnotcovered: Optional[str] = None
    courseid: Optional[int] = None

    class Config:
        orm_mode = True
from pydantic import BaseModel,constr, conint, EmailStr, Field
from datetime import datetime, date
from typing import Optional, List
from pydantic_settings import BaseSettings


class UserCreate(BaseModel):
    username: str  
    password: str  

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str  # JWT token
    token_type: str  # The type of token (usually "bearer")


class Batch(BaseModel):
    batchname: str
    courseid: str
    created_at: Optional[datetime]  # If applicable
    updated_at: Optional[datetime]  # If applicable

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

class LeadCreate(LeadBase):
    pass

class LeadUpdate(LeadBase):
    pass

class LeadResponse(LeadBase):
    leadid: int

    class Config:
        orm_mode = True


class LeadBase(BaseModel):
    name: str
    phone: str
    email: str
    sourcename: Optional[str] = None
    course: Optional[str] = None
    status: Optional[str] = None
    secondaryemail: Optional[str] = None
    secondaryphone: Optional[str] = None
    address: Optional[str] = None
    spousename: Optional[str] = None
    spouseemail: Optional[str] = None
    spousephone: Optional[str] = None
    spouseoccupationinfo: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None


class LeadInDB(BaseModel):
    leadid: int  # Use 'leadid' instead of 'id'
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

class LeadCreate(BaseModel):
    name: str
    email: str
    secondaryemail: Optional[str] = None
    secondaryphone: Optional[str] = None
    address: Optional[str] = None
    spousename: Optional[str] = None
    spouseemail: Optional[str] = None
    spousephone: Optional[str] = None
    spouseoccupationinfo: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

class LeadResponse(BaseModel):
    id: int
    name: str
    email: str
    secondaryemail: Optional[str] = None
    secondaryphone: Optional[str] = None
    address: Optional[str] = None
    spousename: Optional[str] = None
    spouseemail: Optional[str] = None
    spousephone: Optional[str] = None
    spouseoccupationinfo: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

    class Config:
        from_attributes = True

class LeadSearchResponse(BaseModel):  # Add this to avoid the AttributeError
    totalRows: int
    data: List[LeadBase]  # Assuming data is a list of leads

    class Config:
        orm_mode = True



class UserCreate(BaseModel):
    username: str  
    password: str  

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str  # JWT token
    token_type: str  # The type of token (usually "bearer")


class Batch(BaseModel):
    batchname: str
    courseid: str
    created_at: Optional[datetime]  # If applicable
    updated_at: Optional[datetime]  # If applicable

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
    name: str
    email: EmailStr
    phone: str
    course: str
    batchname: str
    enrolleddate: date
    status: str
    diceflag: Optional[bool] = None
    education: Optional[str] = None
    workstatus: Optional[str] = None
    dob: Optional[date] = None
    portalid: Optional[str] = None
    agreement: Optional[bool] = None
    driverslicense: Optional[bool] = None
    workpermit: Optional[bool] = None
    wpexpirationdate: Optional[date] = None
    offerletterurl: Optional[str] = None
    ssnvalidated: Optional[bool] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip: Optional[str] = None
    emergcontactname: Optional[str] = None
    emergcontactemail: Optional[EmailStr] = None
    emergcontactphone: Optional[str] = None
    emergcontactaddrs: Optional[str] = None
    guidelines: Optional[str] = None
    term: Optional[str] = None
    referralid: Optional[int] = None
    salary0: Optional[float] = None
    salary6: Optional[float] = None
    salary12: Optional[float] = None
    originalresume: Optional[str] = None
    notes: Optional[str] = None

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
    current: constr(min_length=1, max_length=1)  # Accepts 'Y' or 'N'
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
        from_attributes = True
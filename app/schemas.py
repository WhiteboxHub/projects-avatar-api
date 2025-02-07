from pydantic import BaseModel,constr, conint
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
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    course: Optional[str]
    batchname: Optional[str]
    enrolleddate: Optional[datetime]
    status: Optional[str]
    diceflag: Optional[int]
    education: Optional[str]
    workstatus: Optional[str]
    dob: Optional[datetime]
    portalid: Optional[str]
    agreement: Optional[str]
    driverslicense: Optional[str]
    workpermit: Optional[str]
    wpexpirationdate: Optional[datetime]
    offerletterurl: Optional[str]
    ssnvalidated: Optional[int]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    zip: Optional[str]
    emergcontactname: Optional[str]
    emergcontactemail: Optional[str]
    emergcontactphone: Optional[str]
    emergcontactaddrs: Optional[str]
    guidelines: Optional[str]
    term: Optional[str]
    referralid: Optional[str]
    salary0: Optional[float]
    salary6: Optional[float]
    salary12: Optional[float]
    originalresume: Optional[str]
    notes: Optional[str]

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

    # batchname: str
    # courseid: str
    # current: str
    # enddate: str
    # exams: int
    # instructor1: str
    # instructor2: Optional[str] = None  # Optional field
    # instructor3: Optional[str] = None  # Optional field
    # lastmoddatetime: str
    # orientationdate: str
    # startdate: str
    # subject: str
    # topicscovered: str
    # topicsnotcovered: str

    class Config:
        from_attributes = True
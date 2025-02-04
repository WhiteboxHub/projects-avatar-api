from pydantic import BaseModel
from datetime import datetime
from typing import Optional
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

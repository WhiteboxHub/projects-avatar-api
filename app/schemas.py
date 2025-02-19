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

class LeadSearchResponse(BaseModel): 
    data: List[LeadBase]  
    class Config:
        orm_mode = True



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
        from_attributes = True
        orm_mode = True

class CandidateSchema(BaseModel):
    candidateid: int
    name: str
    enrolleddate: Optional[date]
    email: Optional[str]
    course: str
    phone: Optional[str]
    status: Optional[str]
    workstatus: Optional[str]
    education: Optional[str]
    workexperience: Optional[str]
    
    class Config:
        orm_mode = True 
class CandidateSearchBase(BaseModel):
    name: Optional[str] 

    class Config:
        orm_mode = True





# ✅ Schema for creating/updating a PO
class POCreate(BaseModel):
    begindate: date
    enddate: Optional[date]
    rate: float
    overtimerate: Optional[float]
    invoicestartdate: date
    freqtype: str
    frequency: int
    invoicenet: int
    placementid: int
    polink: Optional[str]
    notes: Optional[str]

# ✅ Schema for returning a single PO
class POResponse(POCreate):
    id: int
    lastmoddatetime: datetime

    class Config:
        from_attributes = True  # ✅ FIX: Use from_attributes instead of orm_mode

# ✅ Schema for paginated list response
class POListResponse(BaseModel):
    total: int
    page: int
    limit: int
    data: List[POResponse]  # ✅ FIX: This must contain Pydantic objects, not SQLAlchemy ORM objects

    class Config:
        from_attributes = True  # ✅ FIX: Use from_attributes instead of orm_mode








# from pydantic import BaseModel,constr, conint, EmailStr, Field
# from datetime import datetime, date
# from typing import Optional, List
# from pydantic_settings import BaseSettings


# class UserCreate(BaseModel):
#     username: str  
#     password: str  

# class LoginRequest(BaseModel):
#     username: str
#     password: str

# class Token(BaseModel):
#     access_token: str  
#     token_type: str  
    
# class Batch(BaseModel):
#     batchname: str
#     courseid: str
#     created_at: Optional[datetime]  
#     updated_at: Optional[datetime]  

#     class Config:
#         from_attributes = True  

# class UserCreate(BaseModel):
#     uname: str
#     email: str
#     password: str  

#     class Config:
#         orm_mode = True  

# class UserResponse(BaseModel):
#     id: int
#     uname: str
#     email: str

#     class Config:
#         orm_mode = True 



# class LeadBase(BaseModel):
#     name: str
#     email: str
#     phone: Optional[str] = None

# class LeadCreate(LeadBase):
#     pass

# class LeadUpdate(LeadBase):
#     pass

# class LeadResponse(LeadBase):
#     leadid: int

#     class Config:
#         orm_mode = True


# class LeadBase(BaseModel):
#     name: str
#     phone: str
#     email: str
#     sourcename: Optional[str] = None
#     course: Optional[str] = None
#     status: Optional[str] = None
#     secondaryemail: Optional[str] = None
#     secondaryphone: Optional[str] = None
#     address: Optional[str] = None
#     spousename: Optional[str] = None
#     spouseemail: Optional[str] = None
#     spousephone: Optional[str] = None
#     spouseoccupationinfo: Optional[str] = None
#     city: Optional[str] = None
#     state: Optional[str] = None
#     country: Optional[str] = None


# class LeadInDB(BaseModel):
#     leadid: int 
#     name: str
#     email: str
#     phone: str
#     sourcename: str
#     course: str
#     status: str
#     secondaryemail: str
#     secondaryphone: str
#     address: str
#     spousename: str
#     spouseemail: str
#     spousephone: str
#     spouseoccupationinfo: str
#     city: str
#     state: str
#     country: str
#     class Config:
#         from_attributes = True

# class LeadCreate(BaseModel):
#     name: str
#     email: str
#     secondaryemail: Optional[str] = None
#     secondaryphone: Optional[str] = None
#     address: Optional[str] = None
#     spousename: Optional[str] = None
#     spouseemail: Optional[str] = None
#     spousephone: Optional[str] = None
#     spouseoccupationinfo: Optional[str] = None
#     city: Optional[str] = None
#     state: Optional[str] = None
#     country: Optional[str] = None

# class LeadResponse(BaseModel):
#     id: int
#     name: str
#     email: str
#     secondaryemail: Optional[str] = None
#     secondaryphone: Optional[str] = None
#     address: Optional[str] = None
#     spousename: Optional[str] = None
#     spouseemail: Optional[str] = None
#     spousephone: Optional[str] = None
#     spouseoccupationinfo: Optional[str] = None
#     city: Optional[str] = None
#     state: Optional[str] = None
#     country: Optional[str] = None

#     class Config:
#         from_attributes = True

# class LeadSearchResponse(BaseModel): 
#     data: List[LeadBase]  
#     class Config:
#         orm_mode = True



# class UserCreate(BaseModel):
#     username: str  
#     password: str  

# class LoginRequest(BaseModel):
#     username: str
#     password: str

# class Token(BaseModel):
#     access_token: str  
#     token_type: str  

# class Batch(BaseModel):
#     batchname: str
#     courseid: str
#     created_at: Optional[datetime]  
#     updated_at: Optional[datetime]  
#     class Config:
#         from_attributes = True  

# class UserCreate(BaseModel):
#     uname: str
#     email: str
#     password: str  

#     class Config:
#         orm_mode = True  

# class UserResponse(BaseModel):
#     id: int
#     uname: str
#     email: str

#     class Config:
#         orm_mode = True 




# class CandidateBase(BaseModel):
#     name: str
#     email: EmailStr
#     phone: str
#     course: str
#     batchname: str
#     enrolleddate: date
#     status: str
#     diceflag: Optional[bool] = None
#     education: Optional[str] = None
#     workstatus: Optional[str] = None
#     dob: Optional[date] = None
#     portalid: Optional[str] = None
#     agreement: Optional[bool] = None
#     driverslicense: Optional[bool] = None
#     workpermit: Optional[bool] = None
#     wpexpirationdate: Optional[date] = None
#     offerletterurl: Optional[str] = None
#     ssnvalidated: Optional[bool] = None
#     address: Optional[str] = None
#     city: Optional[str] = None
#     state: Optional[str] = None
#     country: Optional[str] = None
#     zip: Optional[str] = None
#     emergcontactname: Optional[str] = None
#     emergcontactemail: Optional[EmailStr] = None
#     emergcontactphone: Optional[str] = None
#     emergcontactaddrs: Optional[str] = None
#     guidelines: Optional[str] = None
#     term: Optional[str] = None
#     referralid: Optional[int] = None
#     salary0: Optional[float] = None
#     salary6: Optional[float] = None
#     salary12: Optional[float] = None
#     originalresume: Optional[str] = None
#     notes: Optional[str] = None

# class CandidateCreate(CandidateBase):
#     pass

# class CandidateUpdate(CandidateBase):
#     pass

# # class CandidateResponse(CandidateBase):
# #     candidateid: int
# #     pass
# #     class Config:
# #         orm_mode = True

# class CandidateResponse(BaseModel):
#     candidateid: int  # Uses candidateid instead of id
#     name: str
#     email: EmailStr
#     phone: str
#     course: str
#     batchname: str
#     enrolleddate: date
#     status: str

#     class Config:
#         from_attributes = True

# class BatchCreate(BaseModel):
#     batchname: constr(max_length=100)
#     current: constr(min_length=1, max_length=1)  
#     orientationdate: Optional[date] = None
#     subject: constr(max_length=45)
#     startdate: date
#     enddate: Optional[date] = None
#     exams: Optional[conint(ge=0)] = None
#     instructor1: Optional[int] = None
#     instructor2: Optional[int] = None
#     instructor3: Optional[int] = None
#     topicscovered: Optional[str] = None
#     topicsnotcovered: Optional[str] = None
#     courseid: Optional[int] = None


#     class Config:
#         from_attributes = True
#         orm_mode = True

# class CandidateSchema(BaseModel):
#     candidateid: int
#     name: str
#     enrolleddate: Optional[date]
#     email: Optional[str]
#     course: str
#     phone: Optional[str]
#     status: Optional[str]
#     workstatus: Optional[str]
#     education: Optional[str]
#     workexperience: Optional[str]
    
#     class Config:
#         orm_mode = True 
# class CandidateSearchBase(BaseModel):
#     name: Optional[str] 

#     class Config:
#         orm_mode = True





# # # ✅ Schema for creating/updating a PO
# # class POCreate(BaseModel):
# #     begindate: date
# #     enddate: Optional[date]
# #     rate: float
# #     overtimerate: Optional[float]
# #     invoicestartdate: date
# #     freqtype: str
# #     frequency: int
# #     invoicenet: int
# #     placementid: int
# #     polink: Optional[str]
# #     notes: Optional[str]

# # # ✅ Schema for returning a single PO
# # class POResponse(POCreate):
# #     id: int
# #     lastmoddatetime: datetime

# #     class Config:
# #         from_attributes = True  # ✅ FIX: Use from_attributes instead of orm_mode

# # # ✅ Schema for paginated list response
# # class POListResponse(BaseModel):
# #     total: int
# #     page: int
# #     limit: int
# #     data: List[POResponse]  # ✅ FIX: This must contain Pydantic objects, not SQLAlchemy ORM objects

# #     class Config:
# #         from_attributes = True  # ✅ FIX: Use from_attributes instead of orm_mode



# class POCreate(BaseModel):
#     begindate: date
#     enddate: Optional[date]
#     rate: float
#     overtimerate: Optional[float]
#     invoicestartdate: date
#     freqtype: str
#     frequency: int
#     invoicenet: float
#     placementid: int
#     polink: Optional[str]
#     notes: Optional[str]

# class POResponse(POCreate):
#     id: int
#     lastmoddatetime: datetime

#     class Config:
#         from_attributes = True  

# class POListResponse(BaseModel):
#     total: int
#     page: int
#     limit: int
#     data: List[POResponse]

#     class Config:
#         from_attributes = True  
        
        
# class VendorBase(BaseModel):
#     companyname: str
#     status: Optional[str] = "Current"
#     accountnumber: Optional[str] = None
#     tier: Optional[int] = 2
#     email: str
#     phone: str
#     fax: Optional[str] = "000-000-0000"
#     address: Optional[str] = None
#     city: Optional[str] = None
#     state: Optional[str] = None
#     country: Optional[str] = None
#     zip: Optional[str] = None
#     url: Optional[str] = "http://nothing.com"
#     solicited: Optional[str] = "N"
#     hirebeforeterm: Optional[str] = "N"

# class VendorCreate(VendorBase):
#     pass

# class VendorUpdate(VendorBase):
#     pass

# class VendorResponse(VendorBase):
#     id: int

#     class Config:
#         from_attributes = True  # Pydantic v2 compatible        
        
        
        
#         # Shared properties for Client
# class ClientBase(BaseModel):
#     companyname: str = Field(..., max_length=250)
#     tier: Optional[int] = 2
#     status: Optional[str] = "Current"
#     email: EmailStr
#     phone: Optional[str] = "000-000-0000"
#     fax: Optional[str] = "000-000-0000"
#     address: Optional[str]
#     city: Optional[str]
#     state: Optional[str]
#     country: Optional[str]
#     zip: Optional[str]
#     url: Optional[str] 
#     manager1name: Optional[str]
#     twitter: Optional[str]
#     facebook: Optional[str]
#     linkedin: Optional[str]
#     manager1email: Optional[EmailStr]
#     manager1phone: Optional[str]
#     hmname: Optional[str]
#     hmemail: Optional[EmailStr]
#     hmphone: Optional[str]
#     hrname: Optional[str]
#     hremail: Optional[EmailStr]
#     hrphone: Optional[str]
#     notes: Optional[str]


# # Schema for creating a Client
# class ClientCreate(ClientBase):
#     companyname: str  # Required


# # Schema for updating a Client
# class ClientUpdate(ClientBase):
#     pass


# # Schema for returning a Client in responses
# class ClientResponse(ClientBase):
#     id: int
#     lastmoddatetime: datetime

#     class Config:
#         from_attributes = True  # Replaces orm_mode in Pydantic v2
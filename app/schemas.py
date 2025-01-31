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

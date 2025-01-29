from pydantic import BaseModel

class UserCreate(BaseModel):
    uname: str  
    passwd: str  

class UserLogin(BaseModel):
    uname: str  
    passwd: str  

class Token(BaseModel):
    access_token: str  # JWT token
    token_type: str  # The type of token (usually "bearer")

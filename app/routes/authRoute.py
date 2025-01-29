from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.controllers.auth_controller import (
    get_user_by_uname,  # Function to get user by username
    verify_md5_hash,    # Function to verify passwords with MD5
    create_access_token,  # Function to create JWT tokens
)
from app.schemas import UserLogin  # Ensure that the schema for UserLogin is correctly imported

router = APIRouter()

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Fetch the user from the database by username
    db_user = get_user_by_uname(db, user.uname)
    
    # Debugging: log the user fetched from the database
    print(f"User fetched from DB: {db_user}")  # Log the user object
    
    # Check if the user exists in the database
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    # Verify the password using MD5 hashing
    if not verify_md5_hash(user.passwd, db_user.passwd):  # Using MD5 verification
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    # Debugging: log password verification result
    print(f"Password verification successful: {verify_md5_hash(user.passwd, db_user.passwd)}")
    
    # Determine the message based on the user's team (Admin, Instructor, etc.)
    if db_user.team == "admin":
        message = "Welcome back admin"
    elif db_user.team == "instructor":
        message = "Welcome back instructor"
    else:
        message = "Welcome back user"
    
    # Generate JWT token
    token = create_access_token(data={"id": db_user.id, "username": db_user.uname})
    
    # Return the token and the role-based message
    return {"token": token, "message": message}

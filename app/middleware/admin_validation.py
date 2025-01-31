from fastapi import Depends, HTTPException, Request
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.database.db import get_db  # Assuming you have a function to get the DB session
from app.config import settings
from app.models import User  # Assuming you have an ORM model for authuser

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"  # Typically this is set to "HS256"

def admin_validation(request: Request, db: Session = Depends(get_db)):
    auth_header = request.headers.get("AuthToken")  # Get token from headers
    
    if not auth_header:
        raise HTTPException(status_code=401, detail="Token not provided")
    
    # Extract token (handle Bearer token and plain token)
    token = auth_header.split(" ")[1] if " " in auth_header else auth_header
    
    try:
        # Decode token and check expiration
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = decoded_token.get("username")
        
        # Ensure the token has the necessary claims
        if username is None:
            raise HTTPException(status_code=403, detail="Token does not have a valid 'username' claim")
        
    except JWTError as e:
        # Check if token is expired
        if "expired" in str(e):
            raise HTTPException(status_code=401, detail="Token has expired")
        raise HTTPException(status_code=403, detail="Invalid or expired token")
    
    # Check if the user exists in the database
    user = db.query(User).filter(User.uname == username).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    request.state.user = user  # Attach the user data to the request object
    return user

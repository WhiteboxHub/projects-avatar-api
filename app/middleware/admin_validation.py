from fastapi import Depends, HTTPException, Request
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.database.db import get_db  # Function to get the DB session
from app.config import settings
from app.models import User,Candidate  # ORM model for authuser

SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"  # Token signing algorithm


def admin_validation(request: Request, db: Session = Depends(get_db)):
    auth_header = request.headers.get("Authtoken")
    
    if not auth_header:
        raise HTTPException(status_code=401, detail="Token not provided")

    token = auth_header.split(" ")[1] if "Bearer" in auth_header else auth_header.split(" ")[0]

    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = decoded_token.get("username")

        if not username:
            raise HTTPException(status_code=403, detail="Token missing 'username' claim")

    except JWTError as e:
        error_message = str(e).lower()
        if "expired" in error_message:
            raise HTTPException(status_code=401, detail="Token has expired")
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    user = db.query(Candidate).filter(Candidate.name == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    request.state.user = user
    return user




# def admin_validation(request: Request, db: Session = Depends(get_db)):
#     """
#     Middleware function to validate admin access based on JWT authentication.
#     """

#     # Retrieve AuthToken from request headers
#     auth_header = request.headers.get("Authorization")
    
#     if not auth_header:
#         raise HTTPException(status_code=401, detail="Token not provided")

#     # Handle Bearer token format or plain token
#     token = auth_header.split(" ")[1] if "Bearer" in auth_header else auth_header.split(" ")[0]

#     try:
#         # Decode JWT token
#         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username = decoded_token.get("username")

#         # Ensure token contains a valid username
#         if not username:
#             raise HTTPException(status_code=403, detail="Token missing 'username' claim")

#     except JWTError as e:
#         error_message = str(e).lower()
#         if "expired" in error_message:
#             raise HTTPException(status_code=401, detail="Token has expired")
#         raise HTTPException(status_code=403, detail="Invalid or expired token")

#     # Verify user existence in the database
#     user = db.query(User).filter(User.uname == username).first()

#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Attach user object to request state
#     request.state.user = user
#     return user

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from typing import Optional
from pydantic import BaseModel
from app.models import User

# OAuth2PasswordBearer will be used to extract the token from the request header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Secret key to decode the JWT token (This should be same as the one used for encoding)
SECRET_KEY = "your_secret_key"  # Set your secret key here
ALGORITHM = "HS256"  # This should match the algorithm used during token creation


# Function to verify the token and extract user info
def verify_token(token: str = Depends(oauth2_scheme)) -> User:
    try:
        # Decode the JWT token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = User(username=payload.get("username"), email=payload.get("email"))
        if user.username is None or user.email is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token: Missing user info",
            )
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token"
        )

from passlib.context import CryptContext
from datetime import datetime,timezone,timedelta
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session
from models3 import User
from database2 import get_db
from fastapi import Depends,HTTPException,status

from jose import jwt,JWTError
SECRET_KEY="Your Secret key"
Algorithm="HS256"
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/login")

def hash_password(plain_password):
    return pwd_context.hash(plain_password)
def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict):
    to_encode=data.copy()

    expire=datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })

    token=jwt.encode(to_encode,SECRET_KEY,algorithm=Algorithm)

    return token

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):

    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[Algorithm])

        email=payload.get("sub")
        if not email:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )
        user=db.execute(select(User).where(User.email==email)).scalar_one_or_none()
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid token" 
            )
        return user
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token or expired tokens"
        )


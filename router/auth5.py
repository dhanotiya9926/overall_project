from fastapi import APIRouter,Depends,HTTPException,status
from schemas import UserCreate,UserResponse,UserLogin,Usertoken
from sqlalchemy.orm import Session
from sqlalchemy import select
from database2 import get_db
from models3 import User
from security4 import hash_password,verify_password,create_access_token,get_current_user

router=APIRouter()

@router.post("/register",response_model=UserResponse)
def register(user_data:UserCreate,db:Session=Depends(get_db)):

    user_existing=db.execute(select(User).where(User.email==user_data.email)).scalar_one_or_none()

    if user_existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User Already Exists with this email"
        )

    hashed_password=hash_password(user_data.password)

    user=User(
        full_name=user_data.full_name,
        email=user_data.email,
        hash_password=hashed_password

    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
@router.post("/login")
def login(user:UserLogin,db:Session=Depends(get_db)):
    db_user=db.execute(select(User).where(User.email==user.email)).scalar_one_or_none()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email and password"
        )
    is_valid=verify_password(user.password,db_user.hash_password)
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email and password"
        )
    data={
        "sub":db_user.email,
        "id":db_user.id
    }
    access_token=create_access_token(data)

    return {
        "Message":"Login Successful",
        "token":access_token
    }
@router.get("/profile",response_model=Usertoken)
def profile(current_user:User=Depends(get_current_user)):
    return current_user
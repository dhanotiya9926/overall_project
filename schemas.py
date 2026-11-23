from pydantic import BaseModel,EmailStr,ConfigDict
from datetime  import datetime

class UserCreate(BaseModel):
    full_name:str
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    full_name:str
    email:EmailStr

model_config=ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Usertoken(BaseModel):
    full_name:str
    id:int
    email:EmailStr
    updated_at:datetime
    created_at:datetime



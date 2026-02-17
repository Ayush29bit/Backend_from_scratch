from pydantic import BaseModel, EmailStr, Field 
from typing import Optional 

class UserCreate(BaseModel):
    email:str
    username:str = Field(min_length=3 max_length=20)
    age : int = Field(ge=13, le=120)
    role:str = Field(default="user")
    bio: Optional[str] = None

class UserReplace(BaseModel):
    username : str = Field(min_length=3, max_length=20)
    email: EmailStr
    age: int = Field(ge=13, le=120)
    role: str = Field(default = "user")
    bio: Optional[str] = None

class UserUpdate(BaseModel):
    username : Optional[str] = Field(min_length=3 , max_length=20)
    email: Optional[EmailStr]    
    age: Optional[int] = Field(ge=13, le=120)
    role: Optional[str] = Field(default = "user")


class UserResponse(BaseModel):
    id : int
    username : str
    email : EmailStr
    age : int 
    role : str
    bio : Optional[str]
    created_at : str
    updated_at : str
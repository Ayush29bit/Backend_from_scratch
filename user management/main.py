from fastapi import FastAPI, HTTPException, status 
from pydantic import BaseModel, EmailStr, Field 
from typing import Optional 
from datetime import datetime

app = FastAPI()

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


from fastapi import FastAPI, HTTPException, status 
from pydantic import BaseModel, EmailStr, Field 
from typing import Optional 
from datetime import datetime
from user_db import users_db
from schema import UserCreate, UserReplace, UserUpdate, UserResponse

app = FastAPI()

@app.get("/users",
         response_model=list[UserResponse],
         status_code=status.HTTP_200_OK)
def get_all_users(skip : int = 0, limit : int = 10, role : Optional[str] = None):
    
    users = list(users_db.values())
    if role:
        users = [user for user in users if user["role"] == role]
    return users[skip: skip + limit]

@app.get("/users/{user_id}",
         response_model=UserResponse,
         status_code=status.HTTP_200_OK)
def get_user(user_id:int)
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return users_db[user_id]

@app.get("/users/search",
         response_model=list[UserResponse],
         status_code=status.HTTP_200_OK)
def search_users(query:str)
    result = []
    for user in users_db.values():
        if query.lower() in user["username"].lower() or query.lower() in user["email"].lower():
            result.append(user)
            return result
    

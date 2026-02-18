from fastapi import FastAPI, HTTPException, status 
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
    
@app.post("/users", response_model = UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data:UserCreate):

    global next_id
    existing_usernames = [u["username"] for u in users_db.values()]
    if user_data.username in existing_usernames:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )

    existing_emails = [u["email"] for u in users_db.values()]
    if user_data.email in existing_emails:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    now = datetime.utcnow().isoformat()
    new_user = {
        "id": next_id,
        "username": user_data.username,
        "email": user_data.email,
        "age": user_data.age,
        "role": user_data.role,
        "bio": user_data.bio,
        "created_at": now,
        "updated_at": now
    }
    
    users_db[next_id] = new_user
    next_id += 1
    
    return new_user

@app.put("/users/{user_id}",
         response_model=UserResponse,
         status_code=status.HTTP_200_OK)    
def replace_user(user_id : int, user_data:UserReplace):
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    existing_usernames = [u["username"] for u in users_db.values() if u["id"] != user_id]
    if user_data.username in existing_usernames:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )

    existing_emails = [u["email"] for u in users_db.values() if u["id"] != user_id]
    if user_data.email in existing_emails:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    now = datetime.utcnow().isoformat()
    updated_user = {
        "id": user_id,
        "username": user_data.username,
        "email": user_data.email,
        "age": user_data.age,
        "role": user_data.role,
        "bio": user_data.bio,
        "created_at": users_db[user_id]["created_at"],
        "updated_at": now
    }
    
    users_db[user_id] = updated_user
    return updated_user

@app.patch("/users/{user_id}",
               response_model = UserResponse,
               status_code=status.HTTP_200_OK)
def update_user(user_id : int, user_data:UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    existing_usernames = [u["username"] for u in users_db.values() if u["id"] != user_id]
    if user_data.username and user_data.username in existing_usernames:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )

    existing_emails = [u["email"] for u in users_db.values() if u["id"] != user_id]
    if user_data.email and user_data.email in existing_emails:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    user = users_db[user_id]
    
    updated_user = {
        "id": user_id,
        "username": user_data.username or user["username"],
        "email": user_data.email or user["email"],
        "age": user_data.age if user_data.age is not None else user["age"],
        "role": user_data.role or user["role"],
        "bio": user_data.bio or user["bio"],
        "created_at": user["created_at"],
        "updated_at": datetime.utcnow().isoformat()
    }
    
    users_db[user_id] = updated_user
    return updated_user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id : int):
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    del users_db[user_id]
    


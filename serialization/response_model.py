from fastapi import APIRouter
from .schemas import UserResponse

router = APIRouter()

@router.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    # pretend this came from DB
    user = {
        "id": user_id,
        "email": "test@example.com",
        "name": "John",
        "created_at": "2024-01-01T00:00:00"
    }
    return user

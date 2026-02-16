from fastapi import APIRouter

user_router = APIRouter(prefix="/users")

@user_router.get("/")
def list_users():
    return []

@user_router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}

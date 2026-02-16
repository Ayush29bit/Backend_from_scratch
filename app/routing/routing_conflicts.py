from fastapi import APIRouter

router = APIRouter()

@router.get("/users/{id}")
def user_by_id(id: int):
    return {"id": id}

@router.get("/users/me")
def current_user():
    return {"me": True}

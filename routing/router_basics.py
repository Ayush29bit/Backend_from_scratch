from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/ping")
def ping_post():
    return {"message": "pong via POST"}

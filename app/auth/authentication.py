from fastapi import APIRouter, HTTPException, status
from auth.hashing import verify_password
from auth.jwt_handler import create_access_token
from architecture.user_service import UserService

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
def login(email: str, password: str):
    users = UserService.list_users()
    user = next((u for u in users if u["email"] == email), None)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(password, user.get("password_hash", "")):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user["id"])})
    return {"access_token": token, "token_type": "bearer"}

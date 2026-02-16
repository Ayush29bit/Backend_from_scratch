from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    age: int
    name: str

    @field_validator("age")
    def validate_age(cls, v):
        if v < 18:
            raise ValueError("User must be at least 18")
        return v

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    created_at: datetime

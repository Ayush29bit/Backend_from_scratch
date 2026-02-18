from datetime import datetime

users_db = {
    1: {
        "id": 1,
        "username": "john",
        "email": "john@example.com",
        "is_active": True,
        "is_verified": False,
        "role": "user",
        "balance": 100.0,
        "created_at": datetime.utcnow().isoformat()
    }
}
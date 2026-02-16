from fastapi import APIRouter

router=APIRouter()

@router.get("/users/{user_id}")
def get_usesr(user_id:int,active:bool=True):
    return{
        "user_id":user_id,
        "active":active
    }


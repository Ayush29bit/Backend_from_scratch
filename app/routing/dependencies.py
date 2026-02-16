from fastapi import APIRouter, Depends

router = APIRouter()

def common_dependency():
    return "shared-value"

@router.get("/items")
def get_items(dep=Depends(common_dependency)):
    return {"dep": dep}

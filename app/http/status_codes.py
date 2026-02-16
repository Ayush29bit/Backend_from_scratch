from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/ok")
def ok():
    return {"message": "All good"}

@router.get("/bad-request")
def bad_request():
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid input"
    )

@router.get("/not-found")
def not_found():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Resource not found"
    )

@router.get("/server-error")
def server_error():
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Something went wrong"
    )

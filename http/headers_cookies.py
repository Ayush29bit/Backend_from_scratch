from fastapi import APIRouter, Request, Response 

router = APIRouter()

@router.get("/read-headers")
def read_headers(request:Request):
    return{
        "user_agent":request.headers.get("user-agent"),
        "accept":request.headers.get("accept"),
    }

@router.get("/set_header")
def set_header(response:Response):
    response.headers["X-App-version"]="1.0.0"
    return {"message":"Header set"}

@router.get("/set-cookie")
def set_cookie(response:Response):
    response.set_cookie(key="session_id",value="abc123")
    return {"message":"Cookie set"}

@router.get("/read-cookie")
def read_cookie(request:Request):
    return {"session_id":request.cookies.get("session id")}
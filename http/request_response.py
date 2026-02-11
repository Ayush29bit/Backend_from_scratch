from fastapi import APIRouter, Request, Response

router = APIRouter()

@router.get("/insept-request")
async def inspect_request(request:Request):
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "query params":dict(request.query_params),
        "client": request.client.host,
    }
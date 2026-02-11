<<<<<<< HEAD
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
=======

from fastapi import APIRouter, Request, Response 

router=APIRouter()

@router.get("/inspect-request")
async def inspect_request(request:Request):
    return{
        "method": request.method,
        "url": str(request.url),
        "query_params": dict(request.query_params),
        "headers": dict(request.headers),
        "client": request.client.host,
    }

@router.post("/custom-response")
async def custom_response():
    response=Response(
        content="Created resource",
        media_type="text/plain",
        status_code=201
    )

    return response
>>>>>>> b0485459b757166266871078db0eb2f3d3adf028

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

router = APIRouter()


# /products

@router.get("/ping")
def ping():
    return ORJSONResponse({
        "msg": "pong"
    })

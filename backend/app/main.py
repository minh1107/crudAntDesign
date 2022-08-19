from fastapi import FastAPI, HTTPException, status
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.types import ASGIApp

from app.api.api_v1.api import api_router
from app.core.config import settings
from helper.error_helper import log_error
from helper.logger_helper import LoggerSimple

logger = LoggerSimple(name=__name__).logger

app = FastAPI()

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


async def handle_auth_error(exc: Exception) -> ASGIApp:
    log_error(exc)
    detail, headers, status_code = "Unauthorized access.", None, status.HTTP_401_UNAUTHORIZED
    if isinstance(exc, HTTPException):
        detail = exc.detail
        status_code = exc.status_code
        headers = exc.headers
    elif isinstance(exc, StarletteHTTPException):
        detail = exc.detail
        status_code = exc.status_code
    return ORJSONResponse(
        {
            "error": {
                "message": detail
            }
        },
        status_code=status_code,
        headers=headers
    )


app.include_router(api_router, prefix=settings.API_PATH)

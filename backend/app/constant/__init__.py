from enum import Enum

from fastapi import HTTPException, status


class HttpExceptionConstant(HTTPException, Enum):
    DATABASE_ERROR = HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Database connection error",
    )

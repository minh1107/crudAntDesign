from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from typing import Optional

from app.models import AuthUser
from app.reuse.defGlob import get_query_output, assignValueToAuthUser
router = APIRouter()
# /users
api_router = APIRouter()




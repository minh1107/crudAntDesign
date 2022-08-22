from typing import Optional
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from app.api.api_v1.endpoints import api_user
from app.reuse.defGlob import get_query_output, assignValueToAuthUser
from app.schemas import AuthUser

api_router = APIRouter()
class ReqBody(BaseModel):
    name: str
    username: str
    email: str
    phone: Optional[str]
    website: Optional[str]
    addressstreet: Optional[str]
    addresssuite: Optional[str]
    addresscity: Optional[str]
    addresszipcode: Optional[str]
    companyname: Optional[str]
    companycatchphrase: Optional[str]
    companybs: Optional[str]

@api_router.get("/users")
async def get_user():
    users = get_query_output(query="select * from users", params={})
    return ORJSONResponse(users)

@api_router.post("/users")
async def post_user(user: ReqBody):
    user_model = AuthUser()
    assignValueToAuthUser(user, user_model, None)
    users = get_query_output(query="select * from users", params={})
    if users:
        return ORJSONResponse(users)
    return ORJSONResponse(False)

@api_router.put('/users/{user_id}', response_model=ReqBody)
async def update_user(user: ReqBody, user_id: str):
    user_model = AuthUser()
    assignValueToAuthUser(user, user_model, user_id)
    users = get_query_output(query="select * from users", params={})
    return ORJSONResponse(users)

@api_router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    get_query_output(query="DELETE FROM users where id=':user_id_1'", params={'user_id_1': user_id})
    users = get_query_output(query="select * from users", params={})
    return ORJSONResponse(users)

api_router.include_router(api_user.router, prefix="/users", tags=["users"])

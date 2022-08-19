import pydantic
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from typing import Optional

from app.api.api_v1.endpoints import api_token, api_product, api_user
from app.controller.control import get_query_output, upsert_lst_user
# from pydantic
import json
import requests

from app.schemas import AuthUser


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

# class ReqBody(BaseModel):
#     key: str
api_router = APIRouter()

@api_router.get("/users")
async def get_root():
    users = get_query_output(query="select * from users", params={})
    return ORJSONResponse(
        # get_query_output(query="select * from users", params={})
        users
    )

@api_router.post("/create/user")
async def create_user(user: ReqBody):
    user_model = AuthUser()
    user_model.name = user.name
    user_model.username = user.username
    user_model.email = user.email
    user_model.phone = user.phone
    user_model.website = user.website
    user_model.addressstreet = user.addressstreet
    user_model.addresssuite = user.addresssuite
    user_model.addresscity = user.addresscity
    user_model.addresszipcode = user.addresszipcode
    user_model.companyname = user.companyname
    user_model.companycatchphrase = user.companycatchphrase
    user_model.companybs = user.companybs
    upsert_lst_user([user_model.dict()])

    users = get_query_output(query="select * from users", params={})
    return ORJSONResponse(
        users
        # print(user)
    )

@api_router.put('/users/{user_id}', response_model=ReqBody)
async def update_user(user: ReqBody, user_id: str):
    user_model = AuthUser()
    print(int(user_id))
    user_model.id = int(user_id)
    user_model.name = user.name
    user_model.username = user.username
    user_model.email = user.email
    user_model.phone = user.phone
    user_model.website = user.website
    user_model.addressstreet = user.addressstreet
    user_model.addresssuite = user.addresssuite
    user_model.addresscity = user.addresscity
    user_model.addresszipcode = user.addresszipcode
    user_model.companyname = user.companyname
    user_model.companycatchphrase = user.companycatchphrase
    user_model.companybs = user.companybs
    print(user_model)
    upsert_lst_user([user_model.dict()])
    users = get_query_output(query="select * from users", params={})
    return ORJSONResponse(
        users
    )

@api_router.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    get_query_output(query="DELETE FROM users where id=':user_id_1'", params={'user_id_1': user_id})
    print(user_id)
    return ORJSONResponse(
        print("Successfuly")
    )


api_router.include_router(api_user.router, prefix="/users", tags=["users"])
api_router.include_router(api_product.router, prefix="/products", tags=["products"])
api_router.include_router(api_token.router, prefix="/tokens", tags=["tokens"])

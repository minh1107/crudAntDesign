from datetime import datetime

from pydantic import BaseModel


class AuthUser(BaseModel):
    id: int = None
    name: str = None
    username: str = None
    email: str = None
    phone: str = None
    website: str = None
    addressstreet: str = None
    addresssuite: str = None
    addresscity: str = None
    addresszipcode: str = None
    companyname: str = None
    companycatchphrase: str = None
    companybs: str = None

    class Config:
        orm_mode = True

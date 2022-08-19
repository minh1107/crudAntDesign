from datetime import datetime

from pydantic import BaseModel


class Token(BaseModel):
    id: int
    jwt_token: str
    user_id: int
    created_at: datetime = None
    expire_at: datetime = None
    is_active: bool = False

    class Config:
        orm_mode = True

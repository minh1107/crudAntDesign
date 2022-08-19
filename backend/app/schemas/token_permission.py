from pydantic import BaseModel


class TokenPermission(BaseModel):
    token_id: int
    endpoint_pattern_id: int

    class Config:
        orm_mode = True

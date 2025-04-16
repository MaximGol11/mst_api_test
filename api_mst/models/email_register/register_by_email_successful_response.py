from pydantic import BaseModel


"""
{
    "status": "ok",
    "data": {
        "username": "asdasdasd@asdasd.fgj",
        "token": "token"
    }
}
"""

class UserData(BaseModel):
    username: str
    token: str


class RegisterResponse(BaseModel):
    status: str
    data: UserData

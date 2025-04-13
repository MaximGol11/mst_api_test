from pydantic import BaseModel


class UserData(BaseModel):
    username: str
    token: str


class RegisterResponse(BaseModel):
    status: str
    data: UserData
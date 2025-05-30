from pydantic import (
    BaseModel,
    Field,
)

"""
{
    "_username": "category_02@test.com",
    "_password": "qweasd",
    "type": "email",
    "_remember_me": "on"
}
"""


class LoginForm(BaseModel):
    username: str = Field(None, serialization_alias="_username")
    password: str = Field(None, serialization_alias="_password")
    register_type: str = Field(None, serialization_alias="type")
    remember_me: str = Field(None, serialization_alias="_remember_me")

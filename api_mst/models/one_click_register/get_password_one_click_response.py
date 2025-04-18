from pydantic import BaseModel


"""
{
  "password": "gMPyaeD7",
  "username": "16118414969883040377@mostbet.com"
}
"""

class GetPasswordOneClickResponse(BaseModel):
    password: str
    username: str

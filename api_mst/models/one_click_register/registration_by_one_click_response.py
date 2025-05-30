from pydantic import BaseModel

"""
{
  "success": true,
  "jwt": "token"
}
"""


class RegistrationByOneClickResponse(BaseModel):
    success: bool
    jwt: str

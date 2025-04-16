from pydantic import BaseModel

"""
{
  "success": true,
  "jwt": "token"
}
"""

class RegistrationByPhoneNumberResponse(BaseModel):
    success: bool
    jwt: str

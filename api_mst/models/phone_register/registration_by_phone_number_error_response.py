from pydantic import BaseModel

"""
{
  "success": true,
  "message": "registration.phone_not_allowed"
}
"""

class RegistrationByPhoneNumberErrorResponse(BaseModel):
    success: bool
    message: str

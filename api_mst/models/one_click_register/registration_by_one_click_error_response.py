from pydantic import BaseModel

"""
{
  "success": true,
  "message": "error_text"
}
"""

class RegistrationByOneClickErrorResponse(BaseModel):
    success: bool
    message: str

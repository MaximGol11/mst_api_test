from typing import List, Dict
from pydantic import BaseModel, Field

"""
{
    "status": "error",
    "errors": {
        "error_codes": [
            "username_already_used"
        ],
        "form_errors": [
            "Это значение уже используется.",
            "Логин уже используется"
        ],
        "email": [
            "Email уже используется"
        ],
        "username": [],
        "plainPassword": [],
        "firstName": [],
        "lastName": [],
        "nickname": [],
        "currencyId": [],
        "phoneNumber": [],
        "country": [],
        "region": [],
        "city": [],
        "phonePrefix": [],
        "registration_method": [],
        "promo": [],
        "oferta_agreement": []
    }
}
"""


class ErrorDetails(BaseModel):
    error_codes: List[str]
    form_errors: List[str]
    email: List[str]
    username: List[str]
    plainPassword: List[str]
    firstName: List[str]
    lastName: List[str]
    nickname: List[str]
    currencyId: List[str]
    phoneNumber: List[str]
    country: List[str]
    region: List[str]
    city: List[str]
    phonePrefix: List[str]
    registration_method: List[str]
    promo: List[str]
    oferta_agreement: List[str]


class ErrorResponse(BaseModel):
    status: str = Field(..., example="error")
    errors: ErrorDetails

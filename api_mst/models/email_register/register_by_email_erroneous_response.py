from typing import List, Dict
from pydantic import BaseModel, Field


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

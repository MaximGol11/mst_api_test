from pydantic import (
    BaseModel,
    Field,
)
from typing import Optional

"""
fos_user_registration_form[countryId]: 10129
fos_user_registration_form[phoneNumber]: 75675675675
fos_user_registration_form[oferta_agreement]: 1
fos_user_registration_form[currencyId]: 6
fos_user_registration_form[plainPassword][first]: qweasd
fos_user_registration_form[plainPassword][second]: qweasd
first_refill_bonus_type_choice: casino
promo_code:
"""


class PlainPassword(BaseModel):
    first: str
    second: str


class PhoneRegistrationForm(BaseModel):
    phone_number: str = Field(..., serialization_alias="fos_user_registration_form[phoneNumber]")
    plain_password: PlainPassword = Field(..., serialization_alias="fos_user_registration_form[plainPassword]")
    currency_id: int = Field(..., serialization_alias="fos_user_registration_form[currencyId]")
    country: int = Field(..., serialization_alias="fos_user_registration_form[countryId]")
    oferta_agreement: int = Field(..., serialization_alias="fos_user_registration_form[oferta_agreement]")
    first_refill_bonus_type_choice: str
    promo_code: Optional[str] = ""

    def to_form(self) -> dict:
        return {
            "fos_user_registration_form[phoneNumber]": self.phone_number,
            "fos_user_registration_form[plainPassword][first]": self.plain_password.first,
            "fos_user_registration_form[plainPassword][second]": self.plain_password.second,
            "fos_user_registration_form[currencyId]": str(self.currency_id),
            "fos_user_registration_form[countryId]": str(self.country),
            "fos_user_registration_form[oferta_agreement]": str(self.oferta_agreement),
            "first_refill_bonus_type_choice": self.first_refill_bonus_type_choice,
            "promo_code": self.promo_code or ""
        }

from typing import Optional
from pydantic import BaseModel, Field

"""
	"fos_user_registration_form[currencyId]": "2",
	"fos_user_registration_form[oferta_agreement]": "1",
	"fos_user_registration_form[countryId]": "10299",
	"first_refill_bonus_type_choice": "casino"
"""

class OneClickRegisterForm(BaseModel):
    currency_id: int = Field(..., serialization_alias="fos_user_registration_form[currencyId]")
    country: int = Field(..., serialization_alias="fos_user_registration_form[countryId]")
    oferta_agreement: int = Field(..., serialization_alias="fos_user_registration_form[oferta_agreement]")
    first_refill_bonus_type_choice: str
    promo_code: Optional[str] = ""


    def to_form(self) -> dict:
        return {
            "fos_user_registration_form[currencyId]": str(self.currency_id),
            "fos_user_registration_form[countryId]": str(self.country),
            "fos_user_registration_form[oferta_agreement]": str(self.oferta_agreement),
            "first_refill_bonus_type_choice": self.first_refill_bonus_type_choice,
            "promo_code": self.promo_code or ""
        }

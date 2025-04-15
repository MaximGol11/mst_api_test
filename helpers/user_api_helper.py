from api_mst.apis.user_api import UserApi
from api_mst.models.email_register.registration_form import (
    RegistrationForm,
    PlainPassword,
)
from api_mst.models.phone_register.phone_registration_form import (
    PhoneRegistrationForm,
    PlainPassword as PhonePlainPassword,
)


class UserApiHelper:

    def __init__(self, user_api: UserApi):
        self.user_api = user_api


    def register_user_by_email(
        self,
        email: str,
        password: str,
        country: int,
        currency_id: int,
        bonus: str,
        positive_response: bool = True,
        **kwargs
    ):
        registration_form = RegistrationForm(
            email=email,
            plain_password=PlainPassword(first=password, second=password),
            currency_id=currency_id,
            country=country,
            oferta_agreement=1,
            first_refill_bonus_type_choice=bonus,
        )
        if positive_response:
            response = self.user_api.post_api_v2_register_json(email_registration_form=registration_form, positive_response=positive_response)
            self.user_api.set_headers({'Authorization': f'Bearer {response.data.token}'})
        else:
            response = self.user_api.post_api_v2_register_json(email_registration_form=registration_form, positive_response=positive_response)
        return response


    def register_user_by_phone(
        self,
        phone_number: str,
        password: str,
        countryId: int,
        currencyId: int,
        bonus: str,
        positive_response: bool = True,
        **kwargs
    ):
        registration_form = PhoneRegistrationForm(
            phone_number=phone_number,
            plain_password=PhonePlainPassword(first=password, second=password),
            currency_id=currencyId,
            country=countryId,
            oferta_agreement=1,
            first_refill_bonus_type_choice=bonus,
        )
        if positive_response:
            response = self.user_api.post_api_v3_register_mobile_json(phone_registration_form=registration_form, positive_response=positive_response)
            self.user_api.set_headers({'Authorization': f'Bearer {response.data.token}'})
        else:
            response = self.user_api.post_api_v3_register_mobile_json(phone_registration_form=registration_form, positive_response=positive_response)
        return response


    def get_user_profile(self, **kwargs):
        response = self.user_api.get_api_v1_user_json(**kwargs)
        return response

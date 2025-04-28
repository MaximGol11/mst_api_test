import allure
from api_mst.apis.user_api import UserApi
from api_mst.models.email_register.registration_form import (
    RegistrationForm,
    PlainPassword,
)
from api_mst.models.phone_register.phone_registration_form import (
    PhoneRegistrationForm,
    PlainPassword as PhonePlainPassword,
)
from api_mst.models.login_form import LoginForm
from api_mst.models.one_click_register.one_click_register_form import OneClickRegisterForm


class UserApiHelper:

    def __init__(self, user_api: UserApi):
        self.user_api = user_api


    @allure.step("Регистрация пользователя по почте")
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


    @allure.step("Регистрация пользователя по номеру телефона")
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
            self.user_api.set_headers({'Authorization': f'Bearer {response.jwt}'})
        else:
            response = self.user_api.post_api_v3_register_mobile_json(phone_registration_form=registration_form, positive_response=positive_response)
        return response


    @allure.step("Регистрация пользователя в 1 клик")
    def register_user_one_click(
        self,
        currency_id,
        country_id,
        bonus,
        positive_response: bool = True,
        **kwargs
    ):
        one_click_register_form = OneClickRegisterForm(
            currency_id=currency_id,
            country=country_id,
            oferta_agreement=1,
            first_refill_bonus_type_choice=bonus,
            positive_response=positive_response
        )    
        response = self.user_api.post_api_v1_registration_one_click(one_click_register_form=one_click_register_form)
        self.user_api.set_headers({'Authorization': f'Bearer {response.jwt}'})
        return response


    @allure.step("Авторизация пользователя")
    def login_check(
        self,
        email: str = None,
        phone_number: str = None,
        password: str = None,
        register_type: str = None
    ):
        if register_type == "mobile":
            login_form = LoginForm(
                username=phone_number,
                password=password,
                register_type=register_type,
                remember_me="on"
            )
        else:
            login_form = LoginForm(
                username=email,
                password=password,
                register_type=register_type,
                remember_me="on"
            )
        response = self.user_api.post_api_login_check(login_form=login_form)
        self.user_api.set_headers({'Authorization': f'Bearer {response["token"]}'})
        return response




    @allure.step("Получение логина и пароля после регистрации в 1 клик")
    def get_user_login_and_password(self):
        return self.user_api.get_api_v1_registration_one_click_get_password_json()


    @allure.step("Получение данных пользователя")
    def get_user_profile(self, **kwargs):
        response = self.user_api.get_api_v1_user_json(**kwargs)
        return response

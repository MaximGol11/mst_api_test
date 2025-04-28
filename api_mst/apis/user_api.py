from restclient.client import RestClient
from api_mst.models.email_register.registration_form import (RegistrationForm)
from api_mst.models.phone_register.phone_registration_form import PhoneRegistrationForm
from api_mst.models.phone_register.registration_by_phone_number_response import RegistrationByPhoneNumberResponse
from api_mst.models.email_register.register_by_email_successful_response import RegisterResponse
from api_mst.models.email_register.register_by_email_erroneous_response import ErrorResponse
from api_mst.models.one_click_register.one_click_register_form import OneClickRegisterForm
from api_mst.models.one_click_register.registration_by_one_click_response import RegistrationByOneClickResponse
from api_mst.models.one_click_register.get_password_one_click_response import GetPasswordOneClickResponse
from api_mst.models.user_profile import UserProfile
from api_mst.models.login_form import LoginForm
import allure


class UserApi(RestClient):

    @allure.step("Регистрация нового пользователя по email")
    def post_api_v2_register_json(
        self,
        email_registration_form: RegistrationForm,
        positive_response: bool = True,
        **kwargs
    ):
        """
        Регистрация нового пользователя по email c типом регистрации full.

        Args:
            Передаем форм дату, и флаг для разделения позитивного и негативного ответа.

        Returns:
            Получаем ответ успешная ли регистрация и токен.
        """

        response = self.post(
            path="/api/v2/register.json",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=email_registration_form.to_form(),
            **kwargs
            )

        if positive_response:
            return RegisterResponse(**response.json())
        else:
            return ErrorResponse(**response.json())


    @allure.step("Регистрация нового пользователя по номеру телефона с паролем")
    def post_api_v3_register_mobile_json(
        self,
        phone_registration_form: PhoneRegistrationForm,
        positive_response: bool = True,
        **kwargs
    ):
        """
        Регистрация пользователя по номеру телефона.

        """
        response = self.post(
            path="/api/v3/register-mobile.json",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=phone_registration_form.to_form(),
            **kwargs
            )

        if positive_response:
            return RegistrationByPhoneNumberResponse(**response.json())
        else:
            response.raise_for_status()
            return ErrorResponse(**response.json())


    @allure.step("Регистрация нового пользователя в 1 клик")
    def post_api_v1_registration_one_click(
        self,
        one_click_register_form: OneClickRegisterForm,
        positive_response: bool = True,
        **kwargs
    ):
        """
        Регистрация пользователя в один клик.

        """
        response = self.post(
            path="/api/v1/registration/one_click",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=one_click_register_form.to_form(),
            **kwargs
        )
        return RegistrationByOneClickResponse(**response.json())


    @allure.step("Получение логина и пароля после регистрации в 1 клик")
    def get_api_v1_registration_one_click_get_password_json(self,
        **kwargs
    ):
        """
        Получение логина и пароля пользователя после регистрации в один клик.

        """
        response = self.get(
            path="/api/v1/registration/one_click/get_password.json",
            **kwargs
        )
        return GetPasswordOneClickResponse(**response.json())



    def get_api_v1_user_status_get_11898(self):
        pass


    def get_api_v1_finance_refill_method_form(self):
        pass


    @allure.step("Получение дааных о пользователе")
    def get_api_v1_user_json(
        self,
        **kwargs
    ):
        """
        Получение информации о пользователе.

        Returns:
            Получаем информацию о пользователе.
        """

        response = self.get(
            path="/api/v1/user.json",
            **kwargs
            )

        return UserProfile(**response.json())


    @allure.step("Авторизация пользователя")
    def post_api_login_check(
        self,
        login_form = LoginForm,
        **kwargs
    ):
        """
        Авторизация пользователя.

        Returns:
            Получаем ответ успешная ли проверка и токен.
        """

        response = self.post(
            path="/api/login_check",
            json=login_form.model_dump(exclude_none=True, by_alias=True),
            **kwargs
        )

        return response.json()

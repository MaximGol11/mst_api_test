from restclient.client import RestClient
from api_mst.models.email_register.registration_form import (RegistrationForm)
from api_mst.models.phone_register.phone_registration_form import PhoneRegistrationForm
from api_mst.models.phone_register.registration_by_phone_number_response import RegistrationByPhoneNumberResponse
from api_mst.models.email_register.register_by_email_successful_response import RegisterResponse
from api_mst.models.email_register.register_by_email_erroneous_response import ErrorResponse
from api_mst.models.user_profile import UserProfile


class UserApi(RestClient):

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
            path="/api/v3/register/mobile.json",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=phone_registration_form.to_form(),
            **kwargs
            )

        if positive_response:
            return RegistrationByPhoneNumberResponse(**response.json())
        else:
            return ErrorResponse(**response.json())


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


    def post_api_login_check(
        self,
        auth_type: str,
        password: str,
        email: str = None,
        phone_number: str = None,
        **kwargs
    ):
        """
        Авторизация пользователя..

        Args:
            email: Email пользователя.
            password: Пароль пользователя.
            phone_number: Номер телефона пользователя.
            **kwargs: Дополнительные параметры запроса.

        Returns:
            Получаем ответ успешная ли проверка и токен.
        """

        if auth_type == "email":
            response = self.post(
                path="/api/login/check",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={"_username": email, "_password": password, "phone_number": phone_number},
                **kwargs
            )
        elif auth_type == "phone":
            response = self.post(
                path="/api/login/check",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={"_username": phone_number, "_password": password},
                **kwargs
            )
        else:
            return {}

        return response.json()

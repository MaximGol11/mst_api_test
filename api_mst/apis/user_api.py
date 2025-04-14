from restclient.client import RestClient
from api_mst.models.email_register.registration_form import (RegistrationForm)
from api_mst.models.email_register.register_by_email_successful_response import RegisterResponse
from api_mst.models.email_register.register_by_email_erroneous_response import ErrorResponse
from api_mst.models.user_profile import UserProfile


class UserApi(RestClient):

    def post_api_v2_register_json(self, email_registration_form: RegistrationForm, positive_response: bool = True, **kwargs):
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


    def get_api_v1_user_json(self, **kwargs):
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

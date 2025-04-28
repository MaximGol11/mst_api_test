import pytest
import allure
from restclient.http_checker import check_status_code_http

@pytest.fixture(params=[
    {"phone_number": "", "password": "qweasd", "currencyId": 2, "countryId": 10297, "bonus": "casino"}, #пустой телефон
    {"phone_number": "421999111991", "password": "", "currencyId": 2, "countryId": 10297, "bonus": "casino"}, #пустой пароль
    {"phone_number": "421999111992", "password": "qweasd", "currencyId": 2, "countryId": 000, "bonus": "casino"}, #пустая страна
    {"phone_number": "421999111993", "password": "qweasd", "currencyId": 000, "countryId": 10297, "bonus": "casino"}, #пустая валюта
    {"phone_number": "421999", "password": "qweasd", "currencyId": 2, "countryId": 10297, "bonus": "casino"}, # не валидный телефон
    {"phone_number": "421999111995", "password": "qwe", "currencyId": 2, "countryId": 10297, "bonus": "casino"}, # не валидный пароль
])
def negative_tests_parametrize_test_data(request):
    return request.param


@allure.suite("Тесты регистрации по номеру телефона с паролем")
class TestPostV3RegisterMobileJson:

    @allure.step("Позитивный тест регистрации по номеру телефона с паролем")
    def test_post_v3_register_mobile_positive(self, user_api_helper, prepare_user_faker):
        phone_number = prepare_user_faker.phone_number
        password = prepare_user_faker.password

        user_api_helper.register_user_by_phone(
            phone_number=phone_number,
            password=password,
            countryId=10297,
            currencyId=2,
            bonus="casino",
            positive_response=True
        )


    @allure.step("Негативные тесты регистрации по номеру телефона с паролем")
    def test_post_v3_register_mobile_negative(self, negative_tests_parametrize_test_data, user_api_helper):
        with check_status_code_http(expected_status_code=400):
            user_api_helper.register_user_by_phone(
                phone_number=negative_tests_parametrize_test_data['phone_number'],
                password=negative_tests_parametrize_test_data['password'],
                currencyId=negative_tests_parametrize_test_data['currencyId'],
                countryId=negative_tests_parametrize_test_data['countryId'],
                bonus=negative_tests_parametrize_test_data['bonus'],
                positive_response=False #приходит негативная форма ответа с ошибкой (нужно будет дополнить, чтобы текст ошибки тоже был в фикстуре)
            )



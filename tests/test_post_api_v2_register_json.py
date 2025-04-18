import pytest


@pytest.fixture(params=[
    {"email": "", "password": "qweasd", "currency": 55, "country": 245, "bonus": "casino"}, #пустой email
    {"email": "test@test.com", "password": "", "currency": 55, "country": 245, "bonus": "casino"}, #пустой пароль
    {"email": "test@test.com", "password": "qweasd", "currency": 55, "country": 000, "bonus": "casino"}, #пустая страна
    {"email": "test@test.com", "password": "qweasd", "currency": 000, "country": 245, "bonus": "casino"}, #пустая валюта
    {"email": "test@test.com", "password": "qweasd", "currency": 55, "country": 245, "bonus": ""}, #пустой бонус
    {"email": "test@test", "password": "qweasd", "currency": 55, "country": 245, "bonus": "casino"}, # не валидный email
    {"email": "test@test.com", "password": "qwe", "currency": 55, "country": 245, "bonus": "casino"}, # не валидный пароль
])
def negative_tests_parametrize_test_data(request):
    return request.param




def test_post_v2_register_json_positive(user_api_helper ,prepare_user_faker):
    email = prepare_user_faker.email
    password = prepare_user_faker.password

    user_api_helper.register_user_by_email(
        email=email,
        password=password,
        currency_id=55,
        country=245,
        bonus="casino",
    )
    response = user_api_helper.get_user_profile()
    assert response.email == email
    print(response)



def test_post_v2_register_json_negative(user_api_helper, negative_tests_parametrize_test_data):
    response = user_api_helper.register_user_by_email(
        email=negative_tests_parametrize_test_data['email'],
        password=negative_tests_parametrize_test_data['password'],
        currency_id=negative_tests_parametrize_test_data['currency'],
        country=negative_tests_parametrize_test_data['country'],
        bonus=negative_tests_parametrize_test_data['bonus'],
        positive_response=False #приходит негативная форма ответа с ошибкой (нужно будет дополнить, чтобы текст ошибки тоже был в фикстуре)
    )

    

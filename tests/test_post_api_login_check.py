import allure


@allure.suite("Тесты проверки авторизации пользователя")
class TestPostApiLoginCheck:

    @allure.step("Позитивный тест проверки авторизации пользователя с номером телефона")
    def test_post_api_login_check_mobile_positive(self, user_api_helper, prepare_user_faker):
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
        user_api_helper.login_check(phone_number=phone_number, password=password, register_type="mobile")


    @allure.step("Негативные тесты тест проверки авторизации пользователя с номером телефона")
    def test_post_api_login_check_mobile_negative(self, ):
        pass


    @allure.step("Позитивный тест проверки авторизации пользователя с почтой")
    def test_post_api_login_check_email_positive(self, user_api_helper, prepare_user_faker):
        email = prepare_user_faker.email
        password = prepare_user_faker.password

        user_api_helper.register_user_by_email(
            email=email,
            password=password,
            currency_id=55,
            country=245,
            bonus="casino",
        )
        user_api_helper.login_check(email=email, password=password, register_type="email")


    @allure.step("Негативный тест проверки авторизации пользователя с почтой")
    def test_post_api_login_check_email_negative(self, ):
        pass



    @allure.step("Позитивный тест проверки авторизации пользователя после регистрации в 1 клик")
    def test_post_api_login_check_one_click(self, user_api_helper):
        user_api_helper.register_user_one_click(currency_id=2, country_id=10297, bonus="casino")
        response = user_api_helper.get_user_login_and_password()

        user_api_helper.login_check(email=response.username, password=response.password, register_type="email")
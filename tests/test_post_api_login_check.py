import allure


@allure.suite("Тесты проверки авторизации пользователя")
class TestPostApiLoginCheck:

    @allure.step("Позитивный тест проверки авторизации пользователя с номером телефона")
    def test_post_api_login_check_mobile_positive(self, ):
        pass


    @allure.step("Негативные тесты тест проверки авторизации пользователя с номером телефона")
    def test_post_api_login_check_mobile_negative(self, ):
        pass


    @allure.step("Позитивный тест проверки авторизации пользователя с почтой")
    def test_post_api_login_check_email_positive(self, ):
        pass


    @allure.step("Позитивный тест проверки авторизации пользователя с почтой")
    def test_post_api_login_check_email_negative(self, ):
        pass
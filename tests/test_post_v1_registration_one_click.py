import allure


@allure.suite("Тесты регистрации в 1 клик")
class TestPostV1RegisterOneClick:

    @allure.step("Тест регистрации в 1 клик")
    def test_post_v1_register_one_click(self, user_api_helper):
        user_api_helper.register_user_one_click(currency_id=2, country_id=10297, bonus="casino")
        response = user_api_helper.get_user_login_and_password()
        user_api_helper.login_check(email=response.username, password=response.password, register_type="email")

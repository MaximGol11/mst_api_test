

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



def test_post_v2_register_json_negative(user_api_helper):
    response = user_api_helper.register_user_by_email(
        email="test1234@test.com",
        password="qweasd",
        currency_id=55,
        country=245,
        bonus="casino",
        positive_response=False
    )

    assert response.errors.error_codes[0] == "username_already_used"

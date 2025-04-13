from api_mst.models.email_register.registration_form import (
    RegistrationForm,
    PlainPassword,
)
import faker


def test_post_v2_register_json(user_api):
    email = faker.Faker().email()
    password = "qweasd"
    
    registration_form = RegistrationForm(
        email=email,
        plain_password=PlainPassword(first=password, second=password),
        currency_id=55,
        country=245,
        oferta_agreement=1,
        first_refill_bonus_type_choice="casino",
    )
    
    response = user_api.post_api_v2_register_json(registration_form)
    print(response)
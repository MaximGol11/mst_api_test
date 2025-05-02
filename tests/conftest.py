import structlog
from collections import namedtuple
from faker import Faker
import pytest
from restclient.configuration import Configuration as UserApiConf
from api_mst.apis.user_api import UserApi
from helpers.user_api_helper import UserApiHelper

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True,
            #sort_keys=True
        )
    ]
)


@pytest.fixture
def user_api():
    user_api_conf = UserApiConf(host="https://dev45.mostbet.com", disable_log=False)
    user = UserApi(user_api_conf)
    return user


@pytest.fixture
def user_api_helper(user_api):
    return UserApiHelper(user_api)


@pytest.fixture
def prepare_user_faker():
    password = Faker().password()
    email = Faker().email()
    phone_number = f"421{Faker().numerify('#########')}"         # пока генерирует только для одной страны, возможно в будующем сделаю генератор под разные страны

    User = namedtuple("User", ["password", "email", "phone_number"])
    user = User(password, email, phone_number)
    return user



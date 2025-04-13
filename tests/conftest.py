import structlog
import pytest
from restclient.configuration import Configuration as UserApiConf
from api_mst.apis.user_api import UserApi

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
    user_api_conf = UserApiConf(host="https://dev48.mostbet.com", disable_log=False)
    user = UserApi(user_api_conf)
    return user


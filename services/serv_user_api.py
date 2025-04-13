from restclient.configuration import Configuration
from api_mst.apis.user_api import UserApi

class UserApi:
    
    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.user_api = UserApi(configuration=self.configuration)
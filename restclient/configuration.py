class Configuration:
    
    def __init__(
        self,
        host: str,
        headers: dict = None,
        disable_log: bool = True,
    ):
        """
        Configuration class to hold the configuration for the REST client.

        Args:
            host (str): The base URL for the REST API.
            headers (dict, optional): Headers to be included in the requests. Defaults to None.
            disable_log (bool, optional): Flag to disable logging. Defaults to True.
        """
        self.host = host
        self.headers = headers if headers is not None else {}
        self.disable_log = disable_log
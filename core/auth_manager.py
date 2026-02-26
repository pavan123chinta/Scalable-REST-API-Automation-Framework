import requests


class AuthManager:
    """
    Handles basic token-based authentication.
    """

    def __init__(self, config_loader):
        self.config = config_loader
        self.auth_enabled = self.config.get_nested("auth", "enabled", default=False)
        self.login_endpoint = self.config.get_nested("auth", "login_endpoint")
        self.username = self.config.get_nested("auth", "username")
        self.password = self.config.get_nested("auth", "password")
        self.token_key = self.config.get_nested("auth", "token_key", default="token")
        self.base_url = self.config.get("base_url")

        self.token = None

    def get_token(self):
        """
        Returns cached token or performs login if token not available.
        """
        if not self.auth_enabled:
            return None

        if self.token:
            return self.token

        return self._login()

    def _login(self):
        """
        Performs login and stores token.
        """
        login_url = f"{self.base_url}{self.login_endpoint}"

        response = requests.post(
            login_url,
            json={
                "username": self.username,
                "password": self.password,
            },
        )

        if response.status_code != 200:
            raise Exception("Authentication failed")

        token = response.json().get(self.token_key)

        if not token:
            raise Exception("Token not found in login response")

        self.token = token
        return self.token
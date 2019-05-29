from requests import request
from .endpoints import Endpoints
from .admin_endpoints import AdminEndpoints


class ApiService:
    def __init__(self):
        self._token = None

    @property
    def token(self):
        """I'm the 'token' property."""
        print("getter of token called")
        return self._token

    @token.setter
    def token(self, value):
        print("setter of token called")
        self._token = value

    default_headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip"
    }

    def auth_headers(self):
        headers = self.default_headers
        headers["Authorization"] = "JWT " + self.token
        return headers

    def _api_call(self, http_method, url, headers, data=None, params=None, **kwargs):
        return request(http_method, url, headers=headers, json=data, params=params, **kwargs)

    def phone_sent_without_code(self, phone):
        url = Endpoints.PHONE_SEND_CONFIRMATION_CODE.value

        data = {
            'phone': phone,
            'should_send_sms': 'false'
        }

        response = self._api_call('post', url, self.default_headers, data)
        return response.json()

    def phone_verify(self, verification_id, code):
        url = Endpoints.PHONE_VERIFY_CODE.value

        data = {
            "verification_id": verification_id,
            "code": code
        }

        response = self._api_call('post', url, self.default_headers, data)
        return response.json()

    def create_ace(self, ace_data):
        url = Endpoints.CREATE_ACE.value
        auth_headers = self.auth_headers()
        response = self._api_call('post', url, auth_headers, ace_data)
        return response.json()

    def upload_giphy(self, giphy_id):
        url = Endpoints.GIPHY_UPLOAD.value
        auth_headers = self.auth_headers()
        data = {
            "giphy_id": giphy_id
        }
        response = self._api_call('post', url, auth_headers, data)
        return response.json()

    def get_user_profile(self):
        url = Endpoints.USER_PROFILE.value
        auth_headers = self.auth_headers()
        response = self._api_call('get', url, auth_headers)
        return response.json()

    def create_flip(self, flip_data):
        url = Endpoints.CREATE_FLIP.value
        auth_headers = self.auth_headers()
        response = self._api_call('post', url, auth_headers, flip_data)
        return response.json()

    """
    ADMIN PANEL REQUESTS
    """
    def get_admin_user_details(self, user_id):
        url = AdminEndpoints.USER_DETAILS.value.format(user_id=user_id)
        auth_headers = self.auth_headers()
        response = self._api_call('get', url, auth_headers)
        return response.json()

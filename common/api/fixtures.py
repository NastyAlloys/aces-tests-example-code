import pytest

from common.settings import FAKE_ADMIN_NUMBER, FAKE_NUMBER, FAKE_SMS_CODE
from common.api.api_service import ApiService


@pytest.fixture()
def api_login():
    api_service = ApiService()
    phone_sent_response = api_service.phone_sent_without_code(FAKE_NUMBER)
    phone_verify_response = api_service.phone_verify(phone_sent_response['verification_id'], FAKE_SMS_CODE)
    token = phone_verify_response['auth_data']['access_token']['token']
    api_service.token = token
    return api_service


@pytest.fixture()
def api_login_as_mutual():
    api_service = ApiService()
    phone_sent_response = api_service.phone_sent_without_code(FAKE_ADMIN_NUMBER)
    phone_verify_response = api_service.phone_verify(phone_sent_response['verification_id'], FAKE_SMS_CODE)
    token = phone_verify_response['auth_data']['access_token']['token']
    api_service.token = token
    return api_service

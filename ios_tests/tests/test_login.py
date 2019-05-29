import pytest

from common.settings import FAKE_SMS_CODE
from common.settings import FAKE_NUMBER
from ..src.page_objects.login_page import LoginPage
from ..src.page_objects.main_page import MainPage


@pytest.mark.critical
def test_login():
    LoginPage().login(FAKE_NUMBER, FAKE_SMS_CODE)
    assert MainPage().is_create_ace_btn_present()

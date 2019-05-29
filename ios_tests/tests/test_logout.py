import pytest

from ..src.page_objects.main_page import MainPage
from ..src.page_objects.user.user_page import UserPage
from ..src.page_objects.user.user_settings_page import UserSettingsPage
from ..src.page_objects.login_page import LoginPage
from ..fixtures import login


@pytest.mark.critical
def test_logout(login):
    MainPage().click_user_profile()
    UserPage().go_to_settings()
    UserSettingsPage().logout()
    assert LoginPage().is_continue_btn_present()

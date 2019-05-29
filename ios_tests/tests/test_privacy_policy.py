import pytest
from hamcrest import assert_that, equal_to

from ..src.page_objects.main_page import MainPage
from ..src.page_objects.user.user_page import UserPage
from ..src.page_objects.user.privacy_policy_web_page import PrivacyPolicyWebPage
from ..src.page_objects.user.user_settings_page import UserSettingsPage

from ..fixtures import login


def test_privacy_policy(login):
    MainPage().click_user_profile()
    UserPage().go_to_settings()
    usp = UserSettingsPage()
    usp.go_to_privacy_policy()

    pp = PrivacyPolicyWebPage()
    pp.scroll_to_first_dropdown_menu()

    pp.open_first_dropdown_menu()
    pp.close_first_dropdown_menu()

    pp.click_done_btn()
    is_user_settings_page_opened = usp.is_opened()

    assert_that(is_user_settings_page_opened, equal_to(True))

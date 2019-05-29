import pytest
from hamcrest import assert_that, equal_to

from ..src.page_objects.main_page import MainPage
from ..src.page_objects.user.user_page import UserPage
from ..src.page_objects.user.tos_page import TOSWebPage
from ..src.page_objects.user.user_settings_page import UserSettingsPage

from ..fixtures import login


def test_tos(login):
    MainPage().click_user_profile()
    UserPage().go_to_settings()
    usp = UserSettingsPage()
    usp.go_to_tos()

    tos = TOSWebPage()
    tos.scroll_to_first_dropdown_menu()

    tos.open_first_dropdown_menu()
    tos.close_first_dropdown_menu()

    tos.click_done_btn()

    is_user_settings_page_opened = usp.is_opened()

    assert_that(is_user_settings_page_opened, equal_to(True))


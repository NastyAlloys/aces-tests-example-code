import pytest
from hamcrest import assert_that, equal_to

from ..src.page_objects.main_page import MainPage
from ..src.page_objects.user.user_page import UserPage
from ..src.page_objects.user.user_settings_page import UserSettingsPage
from ..src.page_objects.user.user_account_page import UserAccountPage

from ..fixtures import login


@pytest.mark.critical
def test_user_account_change(login):
    MainPage().click_user_profile()
    UserPage().go_to_settings()
    UserSettingsPage().go_to_user_account()

    user_account_pg = UserAccountPage()
    first_name_change = user_account_pg.change_first_name()
    last_name_change = user_account_pg.change_last_name()
    user_name_change = user_account_pg.change_user_name()

    assert_that([first_name_change, last_name_change, user_name_change], equal_to([True, True, True]))

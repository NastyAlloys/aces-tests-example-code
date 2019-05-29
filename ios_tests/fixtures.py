import pytest
import random
from .src.page_objects.main_page import MainPage
from .src.page_objects.login_page import LoginPage
from .src.page_objects.user.user_page import UserPage
from .src.page_objects.user.user_settings_page import UserSettingsPage
from .src.page_objects.user.push_notifications_page import PushNotificationsPage

from common.settings import FAKE_NUMBER, FAKE_SMS_CODE


@pytest.fixture(scope="function")
def logout():
    MainPage().click_user_profile()
    UserPage().go_to_settings()
    UserSettingsPage().logout()


@pytest.fixture(scope="function")
def login():
    LoginPage().login(FAKE_NUMBER, FAKE_SMS_CODE)


@pytest.fixture(scope="function")
def reset_all_notifications_switch():
    yield
    push_notif_pg = PushNotificationsPage()
    push_notif_pg.switch_all_notifications(value="1")

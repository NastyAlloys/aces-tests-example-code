import pytest
from hamcrest import assert_that, equal_to

from ..src.page_objects.main_page import MainPage
from ..src.page_objects.user.user_page import UserPage
from ..src.page_objects.user.contact_aces_page import ContactAcesPage
from ..src.page_objects.user.user_settings_page import UserSettingsPage
from common.settings import AcesUser

from ..fixtures import login


def test_contact_aces(login):
    MainPage().click_user_profile()
    UserPage().go_to_settings()
    usp = UserSettingsPage()
    usp.go_to_contact_aces()

    aces_user = AcesUser()
    cap = ContactAcesPage()
    cap.insert_first_name(aces_user.first_name)
    cap.insert_last_name(aces_user.last_name)
    cap.insert_email(aces_user.email)
    cap.select_criticism_subject()

    message = "I love you!"
    cap.insert_message(message)

    cap.click_done_kb_btn()
    cap.scroll_to_send_btn()
    cap.click_send_btn()

    is_success_msg_present = cap.is_success_msg_present()

    cap.click_done_btn()
    is_user_settings_page_opened = usp.is_opened()

    assert_that([is_success_msg_present, is_user_settings_page_opened], equal_to([True, True]))

import pytest
from hamcrest import assert_that, equal_to

from ..src.page_objects.main_page import MainPage
from ..src.page_objects.user.user_page import UserPage
from ..src.page_objects.user.faq_page import FAQPage
from ..src.page_objects.user.user_settings_page import UserSettingsPage

from ..fixtures import login


def test_faq(login):
    MainPage().click_user_profile()
    UserPage().go_to_settings()
    usp = UserSettingsPage()
    usp.go_to_faq()

    faq = FAQPage()
    faq.scroll_to_first_dropdown_menu()
    faq.open_first_dropdown_menu()
    faq.close_first_dropdown_menu()

    faq.click_done_btn()
    is_user_settings_page_opened = usp.is_opened()

    assert_that(is_user_settings_page_opened, equal_to(True))


def test_faq_search(login):
    MainPage().click_user_profile()
    UserPage().go_to_settings()
    usp = UserSettingsPage()
    usp.go_to_faq()

    faq = FAQPage()
    faq.search()

    is_search_result_correct = faq.is_search_result_correct()

    faq.click_done_btn()
    is_user_settings_page_opened = usp.is_opened()

    assert_that([is_search_result_correct, is_user_settings_page_opened], equal_to([True, True]))

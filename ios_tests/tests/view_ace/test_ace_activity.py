import pytest
from hamcrest import assert_that, equal_to

from ios_tests.src.page_objects.main_page import MainPage
from ios_tests.src.page_objects.feeds.my_aces_page import MyAcesPage
from ios_tests.src.page_objects.view_ace.ace_details_page import AceDetailsPage
from ios_tests.src.page_objects.alerts.report_alert import ReportAlert
from ios_tests.src.page_objects.view_ace.flip_activity_page import FlipActivityPage

from common.settings import REPORT_REASON_TEXT
from common.api.api_methods import ApiMethods

from ...fixtures import login
from common.api.fixtures import api_login
from common.api.fixtures import api_login_as_mutual


def test_ace_activity(login):
    MyAcesPage().click_ace_details()
    ace_details_pg = AceDetailsPage()
    ace_details_pg.click_ace_activity()

    flip_activity_pg = FlipActivityPage()
    flip_owner_present = flip_activity_pg.owner_present()
    flip_activity_not_empty = flip_activity_pg.activity_users_present()

    flip_activity_pg.close_activity()

    assert_that([flip_activity_not_empty, flip_owner_present, ace_details_pg.is_opened()],
                equal_to([True, True, True]))


def test_delete_ace_from_ace_activity(login, api_login):
    api_service = api_login
    MainPage().click_my_aces_feed()

    my_aces_pg = MyAcesPage()
    new_ace_id = ApiMethods().create_ace_with_gif(api_service)
    my_aces_pg.page_elements.ace_id = new_ace_id
    my_aces_pg.update_feed()
    my_aces_pg.wait_for_created_ace()
    my_aces_pg.tap_on_created_ace()

    ace_details_pg = AceDetailsPage()
    ace_details_pg.delete_ace()

    my_aces_pg.wait_created_ace_absent()

    assert my_aces_pg.is_ace_present() is False


def test_report_ace(login, api_login, api_login_as_mutual):
    api_service = api_login
    api_service_as_mutual = api_login_as_mutual

    main_pg = MainPage()
    main_pg.click_my_aces_feed()

    my_aces_pg = MyAcesPage()
    new_ace_id = ApiMethods().create_ace_with_gif_as_mutual(api_service, api_service_as_mutual)
    my_aces_pg.page_elements.ace_id = new_ace_id
    my_aces_pg.update_feed()
    my_aces_pg.wait_for_created_ace()
    my_aces_pg.tap_on_created_ace()

    ace_details_pg = AceDetailsPage()
    ace_details_pg.report_ace()

    report_alert = ReportAlert()
    report_alert.fill_additional_info(REPORT_REASON_TEXT)
    report_alert.click_send_btn()
    report_alert.wait_for_done_btn()
    report_alert.wait_for_message(is_flip_alert=False)
    report_alert.click_done_btn()

    assert my_aces_pg.is_opened()


def test_update_flip_feed_and_report_new_flip(login, api_login, api_login_as_mutual):
    api_service = api_login
    api_service_as_mutual = api_login_as_mutual
    MainPage().click_my_aces_feed()

    my_aces_pg = MyAcesPage()
    new_ace_id = ApiMethods().create_ace_with_gif(api_service)
    my_aces_pg.page_elements.ace_id = new_ace_id
    my_aces_pg.update_feed()
    my_aces_pg.wait_for_created_ace()
    my_aces_pg.tap_on_created_ace()

    ace_details_pg = AceDetailsPage()
    new_flip_id = ApiMethods().create_flip_with_gif(api_service_as_mutual, new_ace_id)
    ace_details_pg.page_elements.flip_id = new_flip_id
    ace_details_pg.update_flip_feed()
    ace_details_pg.wait_for_created_flip()
    ace_details_pg.tap_on_created_flip()
    ace_details_pg.report_flip()

    report_alert = ReportAlert()
    report_alert.fill_additional_info(REPORT_REASON_TEXT)
    report_alert.click_send_btn()
    report_alert.wait_for_done_btn()
    report_alert.wait_for_message()
    report_alert.click_done_btn()

    assert my_aces_pg.is_opened() is True


def test_update_flip_feed_and_delete_new_flip(login, api_login, api_login_as_mutual):
    api_service = api_login
    api_service_as_mutual = api_login_as_mutual

    MainPage().click_my_aces_feed()

    my_aces_pg = MyAcesPage()
    new_ace_id = ApiMethods().create_ace_with_gif(api_service)
    my_aces_pg.page_elements.ace_id = new_ace_id
    my_aces_pg.update_feed()
    my_aces_pg.wait_for_created_ace()
    my_aces_pg.tap_on_created_ace()

    ace_details_pg = AceDetailsPage()
    new_flip_id = ApiMethods().create_flip_with_gif(api_service_as_mutual, new_ace_id)
    ace_details_pg.page_elements.flip_id = new_flip_id
    ace_details_pg.update_flip_feed()
    ace_details_pg.wait_for_created_flip()
    ace_details_pg.tap_on_created_flip()
    ace_details_pg.delete_flip(is_mutual=True)

    assert ace_details_pg.is_flip_present() is False


def test_update_flip_feed_and_delete_my_new_flip(login, api_login):
    MainPage().click_my_aces_feed()

    my_aces_pg = MyAcesPage()
    api_service = api_login
    new_ace_id = ApiMethods().create_ace_with_gif(api_service)
    my_aces_pg.page_elements.ace_id = new_ace_id
    my_aces_pg.update_feed()
    my_aces_pg.wait_for_created_ace()
    my_aces_pg.tap_on_created_ace()

    ace_details_pg = AceDetailsPage()
    new_flip_id = ApiMethods().create_flip_with_gif(api_service, new_ace_id)
    ace_details_pg.page_elements.flip_id = new_flip_id
    ace_details_pg.update_flip_feed()
    ace_details_pg.wait_for_created_flip()
    ace_details_pg.tap_on_created_flip()
    ace_details_pg.delete_flip()

    assert ace_details_pg.is_flip_present() is False

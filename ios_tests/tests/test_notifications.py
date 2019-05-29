import pytest

from ..src.page_objects.main_page import MainPage
from ..src.page_objects.user.user_page import UserPage
from ..src.page_objects.user.user_settings_page import UserSettingsPage
from ..src.page_objects.user.push_notifications_page import PushNotificationsPage

from ..fixtures import login
from ..fixtures import reset_all_notifications_switch


@pytest.mark.skip(reason="unstable for unknown reasons")
def test_notifications(login, reset_all_notifications_switch):
    MainPage().click_user_profile()
    UserPage().go_to_settings()
    UserSettingsPage().go_to_push_notifications()

    push_notif_pg = PushNotificationsPage()
    push_notif_pg.switch_random_notifications(count=2)

    before_values = push_notif_pg.get_all_switches_value()

    push_notif_pg.switch_all_notifications(value="0")
    push_notif_pg.wait_for_all_notifications(presence=False)

    push_notif_pg.switch_all_notifications(value="1")
    push_notif_pg.wait_for_all_notifications()

    after_values = push_notif_pg.get_all_switches_value()

    assert before_values == after_values



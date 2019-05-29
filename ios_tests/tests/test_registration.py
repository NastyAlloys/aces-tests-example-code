import pytest

from ios_tests.src.page_objects.alerts.turn_on_notifications_alert import TurnOnNotificationsAlert
from ios_tests.src.page_objects.alerts.allow_notifications_alert import AllowNotificationsAlert

from ..src.page_objects.registration_page import RegistrationPage
from ios_tests.src.page_objects.feeds.everything_feed_page import EverythingFeedPage
from ..src.page_objects.tutorial_page import TutorialPage

from common.settings import FAKE_SMS_CODE
from common.settings import AcesUser


@pytest.mark.critical
@pytest.mark.skip
def test_registration():
    aces_user = AcesUser()
    RegistrationPage().registration(aces_user, FAKE_SMS_CODE)

    TurnOnNotificationsAlert().click_yes()
    AllowNotificationsAlert().click_allow()

    TutorialPage().click_close_btn()

    assert EverythingFeedPage().is_opened()

import pytest

from ios_tests.src.page_objects.user.user_profile_page import UserProfilePage
from ios_tests.src.page_objects.feeds.my_aces_page import MyAcesPage
from ios_tests.src.page_objects.main_page import MainPage

from ...fixtures import login


def test_click_ace_sender(login):
    MainPage().click_my_aces_feed()
    sender_uid = MyAcesPage().click_random_ace_sender()
    user_profile_uid = UserProfilePage().get_user_profile_uid()

    assert sender_uid == user_profile_uid

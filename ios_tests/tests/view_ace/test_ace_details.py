from ios_tests.src.page_objects.view_ace.ace_details_page import AceDetailsPage
from ios_tests.src.page_objects.user.user_profile_page import UserProfilePage
from ios_tests.src.page_objects.feeds.my_aces_page import MyAcesPage
from ios_tests.src.page_objects.main_page import MainPage

from ...fixtures import login


def test_long_press_on_flip_to_get_to_user(login):
    MainPage().click_my_aces_feed()
    MyAcesPage().click_random_ace()

    ace_details_pg = AceDetailsPage()
    flip_owner_id = ace_details_pg.long_press_random_flip()
    user_uid = UserProfilePage().get_user_profile_uid()

    assert flip_owner_id == user_uid

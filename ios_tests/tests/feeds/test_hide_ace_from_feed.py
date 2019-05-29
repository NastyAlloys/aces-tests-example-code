from hamcrest import assert_that, equal_to

from ios_tests.src.page_objects.main_page import MainPage
from ios_tests.src.page_objects.feeds.my_aces_page import MyAcesPage
from ios_tests.src.page_objects.user.user_page import UserPage
from ios_tests.src.page_objects.user.user_settings_page import UserSettingsPage
from ios_tests.src.page_objects.user.account_settings_page import AccountSettingsPage
from ios_tests.src.page_objects.user.hidden_aces_page import HiddenAcesPage

from common.api.api_methods import ApiMethods

from ...fixtures import login
from common.api.fixtures import api_login
from common.api.fixtures import api_login_as_mutual

def test_hide_ace_from_feed(login, api_login, api_login_as_mutual):
    main_pg = MainPage()
    main_pg.click_my_aces_feed()

    api_service = api_login
    api_service_as_mutual = api_login_as_mutual
    new_ace_id = ApiMethods().create_ace_with_gif_as_mutual(api_service, api_service_as_mutual)

    my_aces_pg = MyAcesPage()
    my_aces_pg.page_elements.ace_id = new_ace_id
    my_aces_pg.update_feed()
    my_aces_pg.wait_for_created_ace()
    my_aces_pg.long_tap_on_created_ace()
    my_aces_pg.click_hide_ace_from_feed()
    my_aces_pg.wait_created_ace_absent()

    is_ace_present = my_aces_pg.is_ace_present()

    main_pg.click_user_profile()

    UserPage().go_to_settings()
    UserSettingsPage().go_to_account_settings()
    AccountSettingsPage().go_to_hidden_aces()

    hidden_aces_pg = HiddenAcesPage()
    hidden_aces_pg.page_elements.ace_id = new_ace_id
    hidden_aces_pg.wait_created_ace()

    is_ace_hidden = hidden_aces_pg.is_ace_present()

    assert_that([is_ace_present, is_ace_hidden],
                equal_to([False, True]))

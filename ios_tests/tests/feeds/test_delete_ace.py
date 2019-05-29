from ios_tests.src.page_objects.main_page import MainPage
from ios_tests.src.page_objects.feeds.my_aces_page import MyAcesPage
from ios_tests.src.page_objects.alerts.delete_ace_alert import DeleteAceAlert

from common.api.api_methods import ApiMethods

from ...fixtures import login
from common.api.fixtures import api_login


def test_delete_ace(login, api_login):
    MainPage().click_my_aces_feed()

    api_service = api_login
    new_ace_id = ApiMethods().create_ace_with_gif(api_service)

    my_aces_pg = MyAcesPage()
    my_aces_pg.page_elements.ace_id = new_ace_id
    my_aces_pg.update_feed()
    my_aces_pg.wait_for_created_ace()
    my_aces_pg.long_tap_on_created_ace()
    my_aces_pg.click_delete_ace()

    DeleteAceAlert().click_delete()
    my_aces_pg.wait_created_ace_absent()

    assert my_aces_pg.is_ace_present() is False

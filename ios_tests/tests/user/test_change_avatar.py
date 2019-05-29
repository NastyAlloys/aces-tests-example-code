import pytest

from ...src.page_objects.main_page import MainPage
from ...src.page_objects.user.user_page import UserPage

from ...fixtures import login


@pytest.mark.critical
def test_change_avatar(login):
    main_pg = MainPage()
    main_pg.click_user_profile()
    main_pg.click_my_aces_feed()
    main_pg.click_user_profile()

    user_pg = UserPage()
    user_pg.change_avatar()

    assert user_pg.is_opened()

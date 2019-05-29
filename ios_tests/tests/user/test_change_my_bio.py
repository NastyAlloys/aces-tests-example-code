import pytest

from ...src.page_objects.main_page import MainPage
from ...src.page_objects.user.user_page import UserPage
from common.settings import BIO_TEXT
from common.settings import EMPTY_BIO_TEXT

from hamcrest import assert_that, equal_to
from ...fixtures import login


def test_change_my_bio(login):
    MainPage().click_user_profile()
    user_pg = UserPage()

    user_pg.clear_my_bio()
    empty_bio_field_value = user_pg.get_my_bio()

    user_pg.change_my_bio(BIO_TEXT)
    filled_bio_field_value = user_pg.get_my_bio()

    assert_that([empty_bio_field_value, filled_bio_field_value],
                equal_to([EMPTY_BIO_TEXT, BIO_TEXT]))

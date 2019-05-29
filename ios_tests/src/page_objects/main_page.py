import random
from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.main_page_elements import MainPageElements


class MainPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'create_new_ace_btn', 'Main Page')
        self.page_elements = MainPageElements()

    def is_create_ace_btn_present(self):
        return self.is_element_present_no_error(self.page_elements.create_new_ace_btn)

    def click_user_profile(self):
        self.click_btn(self.page_elements.user_profile_tab_btn)

    def click_my_aces_feed(self):
        self.click_btn(self.page_elements.my_aces_feed_tab_btn)

    def click_everything_feed(self):
        self.click_btn(self.page_elements.everything_feed_tab_btn)

import random

from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.view_ace.flip_activity_elements import FlipActivityElements


class FlipActivityPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'Aces.FlipActivitiesContainerView', 'Flip Activity Page')
        self.page_elements = FlipActivityElements()

    def owner_present(self):
        return self.page_elements.flip_owner.is_present()

    def activity_users_present(self):
        self.wait_presence_element(self.page_elements.activity_users)
        return self.page_elements.activity_users.is_present()

    def close_activity(self):
        self.click_btn(self.page_elements.flip_activity_close_btn)

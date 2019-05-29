from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.user.user_profile_elements import UserProfileElements


class UserProfilePage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'user_profile', "User Profile Page")
        self.page_elements = UserProfileElements()

    def get_user_profile_uid(self):
        return self.page_elements.user_profile.get_value()

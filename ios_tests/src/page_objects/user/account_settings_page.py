from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.user.account_settings_elements import AccountSettingsElements


class AccountSettingsPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.IOS_CLASS_CHAIN,
                         '**/XCUIElementTypeNavigationBar[`name == "Account Settings"`]', "Account Settings Page")
        self.page_elements = AccountSettingsElements()

    def go_to_hidden_aces(self):
        self.click_btn(self.page_elements.hidden_aces_btn)

from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.user.user_settings_page_elements import UserSettingsPageElements


class UserSettingsPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.IOS_CLASS_CHAIN,
                         '**/XCUIElementTypeNavigationBar[`name == "Settings"`]', 'User Settings Page')
        self.page_elements = UserSettingsPageElements()

    def logout(self):
        self.click_logout()
        self.confirm_logout()

    def click_logout(self):
        self.click_btn(self.page_elements.log_out_btn)

    def confirm_logout(self):
        self.click_btn(self.page_elements.confirm_log_out_btn)

    def go_to_user_account(self):
        self.click_btn(self.page_elements.user_account_btn)

    def go_to_push_notifications(self):
        self.click_btn(self.page_elements.push_notifications)

    def go_to_privacy_policy(self):
        self.click_btn(self.page_elements.privacy_policy_btn)

    def go_to_tos(self):
        self.click_btn(self.page_elements.tos_btn)

    def go_to_faq(self):
        self.click_btn(self.page_elements.faq_btn)

    def go_to_contact_aces(self):
        self.click_btn(self.page_elements.contact_btn)

    def go_to_account_settings(self):
        self.click_btn(self.page_elements.account_settings_btn)

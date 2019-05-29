from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.user.hidden_aces_elements import HiddenAcesElements


class HiddenAcesPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.IOS_CLASS_CHAIN,
                         '**/XCUIElementTypeNavigationBar[`name == "Hidden Aces"`]', "Hidden Aces Page")
        self.page_elements = HiddenAcesElements()

    def is_ace_present(self):
        return self.page_elements.ace_by_id.is_present()

    def wait_created_ace(self):
        self.wait_presence_element(self.page_elements.ace_by_id)

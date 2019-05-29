from appium.webdriver.common.mobileby import MobileBy

from common.settings import PRIVACY_POLICY_TEXT_TO_COMPARE
from common.page_objects.base_page import BasePage
from common.page_elements.user.privacy_policy_web_page_elements import PrivacyPolicyPageElements


class PrivacyPolicyWebPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, "Privacy Policy", "Privacy Policy Page")
        self.page_elements = PrivacyPolicyPageElements()

    def scroll_to_first_dropdown_menu(self):
        self.wait_presence_element(self.page_elements.icons)
        first_dropdown_element = self.wait_presence_element(self.page_elements.first_dropdown_element)
        first_dropdown_element.scroll_to_element()
        first_dropdown_element.wait_visibility(False, 10)

    def open_first_dropdown_menu(self):
        plus_btns = self.wait_presence_element(self.page_elements.plus_btn).all_elements
        plus_btns[0].click()

    def is_correct_dropdown_opened(self):
        return self.compare_element_value_with_text(self.page_elements.first_dropdown_description,
                                                    PRIVACY_POLICY_TEXT_TO_COMPARE)

    def close_first_dropdown_menu(self):
        self.click_btn(self.page_elements.minus_btn)

    def click_done_btn(self):
        self.click_btn(self.page_elements.done_btn)

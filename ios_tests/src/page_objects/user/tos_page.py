from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.user.tos_page_elements import TOSPageElements
from common.settings import TOS_TEXT_TO_COMPARE


class TOSWebPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, "Terms of Service", "Terms of Service Page")
        self.page_elements = TOSPageElements()

    def scroll_to_first_dropdown_menu(self):
        self.wait_presence_element(self.page_elements.welcome_text)
        first_dropdown_element = self.wait_presence_element(self.page_elements.first_dropdown_element)
        first_dropdown_element.scroll_to_element()
        first_dropdown_element.wait_visibility(False, 10)

    def open_first_dropdown_menu(self):
        plus_btns = self.wait_presence_element(self.page_elements.plus_btn).all_elements
        plus_btns[0].click()

    def is_correct_dropdown_opened(self):
        return self.compare_element_value_with_text(self.page_elements.first_dropdown_description, TOS_TEXT_TO_COMPARE)

    def close_first_dropdown_menu(self):
        self.click_btn(self.page_elements.minus_btn)

    def click_done_btn(self):
        self.click_btn(self.page_elements.done_btn)

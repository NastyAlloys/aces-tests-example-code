from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.user.faq_page_elements import FAQPageElements
from common.settings import FAQ_TEXT_TO_COMPARE


class FAQPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, "FAQ - Aces", "FAQ Page")
        self.page_elements = FAQPageElements()

    def scroll_to_first_dropdown_menu(self):
        first_dropdown_element = self.wait_presence_element(self.page_elements.first_dropdown_element)
        first_dropdown_element.scroll_to_element()
        first_dropdown_element.wait_visibility(False, 10)

    def open_first_dropdown_menu(self):
        plus_btns = self.wait_presence_element(self.page_elements.plus_btn, 5, True).all_elements
        plus_btns[0].click()

    def is_first_dropdown_opened(self):
        return self.is_element_present_no_error(self.page_elements.minus_btn, 5)

    def is_correct_dropdown_opened(self):
        return self.compare_element_value_with_text(self.page_elements.search_value_result, FAQ_TEXT_TO_COMPARE)

    def close_first_dropdown_menu(self):
        self.click_btn(self.page_elements.minus_btn)

    def search(self):
        self.input_text_in_element(self.page_elements.search_field, "How", True)
        self.click_btn(self.page_elements.search_btn)

    def is_search_result_correct(self):
        return self.compare_element_value_with_text(self.page_elements.search_value_result, FAQ_TEXT_TO_COMPARE)

    def click_done_btn(self):
        self.click_btn(self.page_elements.done_btn)

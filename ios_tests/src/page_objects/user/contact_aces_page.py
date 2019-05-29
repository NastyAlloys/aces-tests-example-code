from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.user.contact_aces_page_elements import ContactAcesPageElements


class ContactAcesPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, "Contact Us", "Contact Us Page")
        self.page_elements = ContactAcesPageElements()

    def insert_first_name(self, f_name):
        self.input_text_in_child_element(self.page_elements.text_fields, 0, f_name)

    def insert_last_name(self, l_name):
        self.input_text_in_child_element(self.page_elements.text_fields, 1, l_name)

    def insert_email(self, email):
        self.input_text_in_child_element(self.page_elements.text_fields, 2, email)

    def select_criticism_subject(self):
        self.select_from_options_dropdown_menu(self.page_elements.reason_select,
                                               self.page_elements.criticism_choice)

    def insert_message(self, msg):
        self.input_text_in_element(self.page_elements.text_view, msg)

    def click_random_acemoji(self):
        self.click_random_sibling_in_parent(self.page_elements.acemoji)

    def click_send_btn(self):
        self.click_btn(self.page_elements.send_btn)

    def is_success_msg_present(self):
        return self.is_element_present_no_error(self.page_elements.success_msg)

    def click_done_btn(self):
        self.click_btn(self.page_elements.done_btn)

    def click_done_kb_btn(self):
        kb_done_btn = self.page_elements.done_btn.all_elements[1]
        kb_done_btn.click()

    def scroll_to_send_btn(self):
        send_btn_element = self.wait_presence_element(self.page_elements.send_btn)
        send_btn_element.scroll_to_element()
        send_btn_element.wait_visibility(False, 10)

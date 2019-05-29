from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.login_page_elements import LoginPageElements
from ios_tests.src.page_objects.alerts.turn_on_notifications_alert import TurnOnNotificationsAlert
from ios_tests.src.page_objects.alerts.allow_notifications_alert import AllowNotificationsAlert


class LoginPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'logo', 'Login Page')
        self.page_elements = LoginPageElements()

    def login(self, phone, sms_code, on_register=False):
        self.click_continue()
        self.set_phone_number(phone)
        self.accept_terms()
        self.get_security_code()
        self.driver.background_app({"timeout": 1})
        self.set_sms_code(sms_code)

        if not on_register:
            TurnOnNotificationsAlert().click_yes()
            AllowNotificationsAlert().click_allow()

    def click_continue(self):
        self.click_btn(self.page_elements.continue_btn)

    def accept_terms(self):
        self.click_btn(self.page_elements.terms_btn)

    def get_security_code(self):
        self.click_btn(self.page_elements.security_code_btn)

    def set_phone_number(self, number):
        self.wait_and_input_text_in_element(self.page_elements.login_phone_field, "+1", number)

    def set_sms_code(self, code):
        self.input_text_in_element(self.page_elements.code_input_field, code, False)

    def is_continue_btn_present(self):
        return self.is_element_present_no_error(self.page_elements.continue_btn)

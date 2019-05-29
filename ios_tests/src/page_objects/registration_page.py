from appium.webdriver.common.mobileby import MobileBy


from common.page_objects.base_page import BasePage
from common.page_elements.registration_page_elements import RegistrationPageElements

from ..page_objects.login_page import LoginPage
from common.settings import AcesUser


class RegistrationPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'logo', 'Registration Page')
        self.page_elements = RegistrationPageElements()

    def registration(self, aces_user: AcesUser, sms_code):
        LoginPage().login(aces_user.phone, sms_code, on_register=True)

        self.set_user_info(aces_user)
        self.click_done()

    def click_enter_invite_code(self):
        self.click_btn(self.page_elements.invite_code_btn)

    def enter_invite_code(self, invite_code):
        self.input_text_in_element(self.page_elements.invite_code_field, invite_code, False)

    def click_submit_invite_code(self):
        self.click_btn(self.page_elements.submit_invite_code)

    def set_user_info(self, aces_user: AcesUser):
        self.set_user_photo()

        self.click_btn(self.page_elements.first_name_field)
        self.input_text_in_element(self.page_elements.first_name_field, aces_user.first_name, False)

        self.click_btn(self.page_elements.last_name_field)
        self.input_text_in_element(self.page_elements.last_name_field, aces_user.last_name, False)

        self.driver.hide_keyboard('Return')

        self.click_btn(self.page_elements.user_name_field)
        self.input_text_in_element(self.page_elements.user_name_field, aces_user.username, False)

        self.click_btn(self.page_elements.birth_date_field)
        self.input_text_in_element(self.page_elements.birth_date_field, aces_user.birth_date, False)

    def set_user_photo(self):
        self.click_btn(self.page_elements.camera_btn)
        self.click_btn(self.page_elements.photo_lib_btn)
        self.click_btn(self.page_elements.camera_roll)
        self.click_photo()
        self.click_btn(self.page_elements.save_btn)

    def click_photo(self):
        self.click_btn(self.page_elements.photo_to_pick)

    def click_done(self):
        self.click_btn(self.page_elements.registration_done_btn)

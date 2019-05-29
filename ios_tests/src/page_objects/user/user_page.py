from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.user.user_page_elements import UserPageElements


class UserPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'user_settings_btn', "User Settings Page")
        self.page_elements = UserPageElements()

    def go_to_settings(self):
        self.click_btn(self.page_elements.user_settings_btn)

    def get_my_bio(self):
        return self.page_elements.bio_field.get_value()

    def change_my_bio(self, bio_text):
        self.click_btn(self.page_elements.bio_edit_btn)
        self.wait_presence_element(self.page_elements.bio_edit_field)
        self.input_text_in_element(self.page_elements.bio_edit_field, bio_text)
        self.page_elements.char_counter_label.wait_text_presence_in_element_value("0")
        self.quit_bio_editing()
        self.page_elements.bio_edit_btn.wait_clickable()

    def clear_my_bio(self):
        self.click_btn(self.page_elements.bio_edit_btn)
        self.page_elements.bio_edit_field.clear_text()
        self.page_elements.char_counter_label.wait_text_presence_in_element_value("160")
        self.quit_bio_editing()
        self.page_elements.bio_edit_btn.wait_clickable()

    def wait_for_empty_bio_text(self, text):
        self.page_elements.bio_field.wait_text_presence_in_element_value(text)

    def get_char_count(self):
        return self.page_elements.char_counter_label.get_value()

    def quit_bio_editing(self):
        self.page_elements.bio_edit_field.click_outside(0, 5)

    def click_edit_button(self):
        self.click_btn(self.page_elements.bio_edit_btn)

    def change_avatar(self):
        self.click_btn(self.page_elements.camera)
        self.click_btn(self.page_elements.photo_library)
        self.click_btn(self.page_elements.camera_roll)
        self.click_btn(self.page_elements.photo_to_pick)
        self.click_btn(self.page_elements.save_btn)
        self.page_elements.progress_hud.wait_element()
        self.page_elements.progress_hud.wait_element_absent()

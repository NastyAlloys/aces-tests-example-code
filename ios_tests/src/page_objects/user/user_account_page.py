from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException

from common.page_objects.base_page import BasePage
from common.page_elements.user.user_account_page_elements import UserAccountPageElements


class UserAccountPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.IOS_CLASS_CHAIN,
                         '**/XCUIElementTypeNavigationBar[`name == "User Profile"`]', "User Profile Page")
        self.page_elements = UserAccountPageElements()

    def change_first_name(self):
        return self.change(self.page_elements.first_name_edit_btn, self.page_elements.first_name_edit_field,
                           self.page_elements.first_name_val)

    def change_last_name(self):
        return self.change(self.page_elements.last_name_edit_btn, self.page_elements.last_name_edit_field,
                           self.page_elements.last_name_val)

    def change_user_name(self):
        return self.change(self.page_elements.user_name_edit_btn, self.page_elements.user_name_edit_field,
                           self.page_elements.user_name_val)

    def click_update(self):
        self.click_btn(self.page_elements.update_btn)

    def change(self, btn_element, edit_field_name, field_name):
        self.click_btn(btn_element)
        new_text = self.reverse_text_in_element(edit_field_name)
        self.click_update()
        try:
            field_name.wait_text_presence_in_element(new_text, 5)
            return True
        except TimeoutException:
            return False

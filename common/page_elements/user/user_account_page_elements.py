from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class UserAccountPageElements(BasePageElements):
    @property
    def first_name_edit_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'first_name_edit_button'),
            'ANDROID': None
        })

    @property
    def last_name_edit_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'last_name_edit_button'),
            'ANDROID': None
        })

    @property
    def user_name_edit_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'user_name_edit_button'),
            'ANDROID': None
        })

    @property
    def first_name_edit_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'first_name_edit_field'),
            'ANDROID': None
        })

    @property
    def last_name_edit_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'last_name_edit_field'),
            'ANDROID': None
        })

    @property
    def user_name_edit_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'user_name_edit_field'),
            'ANDROID': None
        })

    @property
    def first_name_val(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'first_name_value'),
            'ANDROID': None
        })

    @property
    def last_name_val(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'last_name_value'),
            'ANDROID': None
        })

    @property
    def user_name_val(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'user_name_value'),
            'ANDROID': None
        })

    @property
    def update_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Update'),
            'ANDROID': None
        })

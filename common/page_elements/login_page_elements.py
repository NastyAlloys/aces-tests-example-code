from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class LoginPageElements(BasePageElements):
    @property
    def continue_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Continue'),
            'ANDROID': None
        })

    @property
    def terms_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'accept_terms'),
            'ANDROID': None
        })

    @property
    def security_code_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'get_security_code_btn'),
            'ANDROID': None
        })

    @property
    def login_phone_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'login_phone_field'),
            'ANDROID': None
        })

    @property
    def code_input_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'code_input_field'),
            'ANDROID': None
        })

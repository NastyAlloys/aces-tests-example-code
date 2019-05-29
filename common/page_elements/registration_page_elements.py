from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class RegistrationPageElements(BasePageElements):
    @property
    def invite_code_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Enter Invite Code'),
            'ANDROID': None
        })

    @property
    def invite_code_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'invite_code_text_field'),
            'ANDROID': None
        })

    @property
    def submit_invite_code(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Submit Invite Code'),
            'ANDROID': None
        })

    @property
    def first_name_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'first_name_field'),
            'ANDROID': None
        })

    @property
    def last_name_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'last_name_field'),
            'ANDROID': None
        })

    @property
    def user_name_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'username_field'),
            'ANDROID': None
        })

    @property
    def birth_date_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'birth_date_field'),
            'ANDROID': None
        })

    @property
    def registration_done_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'registration_done_btn'),
            'ANDROID': None
        })

    @property
    def camera_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'camera'),
            'ANDROID': None
        })

    @property
    def photo_lib_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Photo library'),
            'ANDROID': None
        })

    @property
    def camera_roll(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Camera Roll'),
            'ANDROID': None
        })

    @property
    def photo_to_pick(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]"),
            'ANDROID': None
        })

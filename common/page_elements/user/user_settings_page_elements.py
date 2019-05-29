from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class UserSettingsPageElements(BasePageElements):
    @property
    def log_out_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Log Out'),
            'ANDROID': None
        })

    @property
    def confirm_log_out_btn(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label BEGINSWITH "Log Out"`]'),
            'ANDROID': None
        })

    @property
    def account_settings_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Account Settings'),
            'ANDROID': None
        })

    @property
    def user_account_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'User Profile'),
            'ANDROID': None
        })

    @property
    def push_notifications(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Push Notifications'),
            'ANDROID': None
        })

    @property
    def privacy_policy_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Privacy Policy'),
            'ANDROID': None
        })

    @property
    def tos_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Terms of Service'),
            'ANDROID': None
        })

    @property
    def faq_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'FAQ'),
            'ANDROID': None
        })

    @property
    def contact_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Contact Aces'),
            'ANDROID': None
        })

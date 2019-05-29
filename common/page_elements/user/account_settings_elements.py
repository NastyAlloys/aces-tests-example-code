from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class AccountSettingsElements(BasePageElements):
    @property
    def hidden_aces_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Hidden Aces'),
            'ANDROID': None
        })

    @property
    def blocked_user_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Blocked Users'),
            'ANDROID': None
        })

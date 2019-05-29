from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class UserProfileElements(BasePageElements):
    @property
    def user_profile(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'user_profile'),
            'ANDROID': None
        })

    @property
    def profile_crown(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'ic_profile_crown'),
            'ANDROID': None
        })

    @property
    def profile_heart(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'ic_profile_heart'),
            'ANDROID': None
        })


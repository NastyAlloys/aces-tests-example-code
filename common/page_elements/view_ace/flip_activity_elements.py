from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class FlipActivityElements(BasePageElements):
    @property
    def flip_activity_close_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'ic flip activity close'),
            'ANDROID': None
        })

    @property
    def activity_users(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeTable/XCUIElementTypeCell"),
            'ANDROID': None
        })

    @property
    def flip_owner(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'flip_owner'),
            'ANDROID': None
        })

    @property
    def flip_owner_name(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'flip_owner_name'),
            'ANDROID': None
        })

    @property
    def flip_owner_date(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'flip_owner_date'),
            'ANDROID': None
        })

    @property
    def flip_owner_image(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'flip_owner_image'),
            'ANDROID': None
        })
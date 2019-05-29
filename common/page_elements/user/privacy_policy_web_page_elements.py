from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class PrivacyPolicyPageElements(BasePageElements):
    @property
    def plus_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, '+'),
            'ANDROID': None
        })

    @property
    def minus_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, '−'),
            'ANDROID': None
        })

    @property
    def done_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Done'),
            'ANDROID': None
        })

    @property
    def first_dropdown_element(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, "1. Collection of Personal Information"),
            'ANDROID': None
        })

    @property
    def icons(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'icons'),
            'ANDROID': None
        })

    @property
    def first_dropdown_description(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label BEGINSWITH "Personal Information includes"'),
            'ANDROID': None
        })

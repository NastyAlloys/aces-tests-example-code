from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class TOSPageElements(BasePageElements):
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
            'IOS': (MobileBy.ACCESSIBILITY_ID, "1. Eligibility"),
            'ANDROID': None
        })

    @property
    def welcome_text(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label BEGINSWITH "Welcome"'),
            'ANDROID': None
        })

    @property
    def first_dropdown_description(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label BEGINSWITH "You may use the Services"'),
            'ANDROID': None
        })

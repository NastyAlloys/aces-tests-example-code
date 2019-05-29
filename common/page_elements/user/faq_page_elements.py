from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class FAQPageElements(BasePageElements):
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
            'IOS': (MobileBy.IOS_PREDICATE, 'label == "How To Use Aces"'),
            'ANDROID': None
        })

    @property
    def search_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label == "search"'),
            'ANDROID': None
        })

    @property
    def search_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'SEARCH'),
            'ANDROID': None
        })

    @property
    def search_value_result(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label BEGINSWITH "“How"'),
            'ANDROID': None
        })

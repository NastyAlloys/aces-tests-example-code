from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class ContactAcesPageElements(BasePageElements):
    @property
    def reason_select(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`value BEGINSWITH "Select Category"`]'),
            'ANDROID': None
        })

    @property
    def criticism_choice(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label == "Criticism"'),
            'ANDROID': None
        })

    @property
    def selected_criticism_choice(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, "Criticism"),
            'ANDROID': None
        })

    @property
    def text_view(self):
        return self._textbox_element({
            'IOS': (MobileBy.CLASS_NAME, "XCUIElementTypeTextView"),
            'ANDROID': None
        })

    @property
    def success_msg(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label BEGINSWITH "Thanks!"'),
            'ANDROID': None
        })

    @property
    def text_fields(self):
        return self._element({
            'IOS': (MobileBy.CLASS_NAME, "XCUIElementTypeTextField"),
            'ANDROID': None
        })

    @property
    def send_btn(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label == "SEND"'),
            'ANDROID': None
        })

    @property
    def acemoji(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label == "acemoji"'),
            'ANDROID': None
        })

    @property
    def done_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Done'),
            'ANDROID': None
        })
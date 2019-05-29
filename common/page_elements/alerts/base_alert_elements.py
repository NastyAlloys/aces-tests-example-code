from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class BaseAlertElements(BasePageElements):
    @property
    def text_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.CLASS_NAME, "XCUIElementTypeTextField"),
            'ANDROID': None
        })

    @property
    def send_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Send'),
            'ANDROID': None
        })

    @property
    def done_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Done'),
            'ANDROID': None
        })

    @property
    def delete_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Delete'),
            'ANDROID': None
        })

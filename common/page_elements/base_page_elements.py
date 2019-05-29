from appium.webdriver.common.mobileby import MobileBy
from caesar.mobile.elements.mobile_element import MobileElement
from caesar.mobile.elements.mobile_text_box import MobileTextBox as TextBox
from common.config import test_run


class BasePageElements:
    def __locator_for_platform(self, selectors):
        return selectors.get(test_run.PLATFORM, 'Undefined Selector')

    def _element(self, selectors):
        return MobileElement(*self.__locator_for_platform(selectors))

    def _textbox_element(self, selectors):
        return TextBox(*self.__locator_for_platform(selectors))

    @property
    def menu_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'menu'),
            'ANDROID': None
        })

    @property
    def back_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Back'),
            'ANDROID': None
        })

    @property
    def cancel_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Cancel'),
            'ANDROID': None
        })

    @property
    def save_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Save'),
            'ANDROID': None
        })

    @property
    def progress_hud(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'SVProgressHUD'),
            'ANDROID': None
        })

    @property
    def pull_to_refresh(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'pull_to_refresh'),
            'ANDROID': None
        })

    @property
    def delete_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Delete'),
            'ANDROID': None
        })

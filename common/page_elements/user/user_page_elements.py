from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class UserPageElements(BasePageElements):
    @property
    def user_settings_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'user_settings_btn'),
            'ANDROID': None
        })

    @property
    def bio_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'user_bio_field'),
            'ANDROID': None
        })

    @property
    def bio_edit_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'ic pencil small'),
            'ANDROID': None
        })

    @property
    def bio_edit_field(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'user_edit_bio_field'),
            'ANDROID': None
        })

    @property
    def char_counter_label(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'char_counter_label'),
            'ANDROID': None
        })

    @property
    def camera(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'camera'),
            'ANDROID': None
        })

    @property
    def user_avatar_image(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'user_avatar_image'),
            'ANDROID': None
        })

    @property
    def photo_library(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Photo library'),
            'ANDROID': None
        })


    @property
    def camera_roll(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Camera Roll'),
            'ANDROID': None
        })

    @property
    def photo_to_pick(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]"),
            'ANDROID': None
        })

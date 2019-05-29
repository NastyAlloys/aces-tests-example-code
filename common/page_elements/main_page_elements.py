from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class MainPageElements(BasePageElements):
    @property
    def create_new_ace_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'create_new_ace_btn'),
            'ANDROID': None
        })

    @property
    def user_profile_tab_btn(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/XCUIElementTypeButton[5]'),
            'ANDROID': None
        })

    @property
    def content_cell_node(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'content_cell_node'),
            'ANDROID': None
        })

    @property
    def header_cell_node(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'header_cell_node'),
            'ANDROID': None
        })

    @property
    def my_aces_feed_tab_btn(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/XCUIElementTypeButton[2]'),
            'ANDROID': None
        })

    @property
    def everything_feed_tab_btn(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/XCUIElementTypeButton[1]'),
            'ANDROID': None
        })
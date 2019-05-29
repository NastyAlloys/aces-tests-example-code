from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.feeds.base_feed_elements import BaseFeedElements


class EverythingFeedElements(BaseFeedElements):
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

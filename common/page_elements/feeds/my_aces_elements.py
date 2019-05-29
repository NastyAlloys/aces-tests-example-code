from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.feeds.base_feed_elements import BaseFeedElements


class MyAcesElements(BaseFeedElements):
    @property
    def feed(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar[`name == "My Aces"`]'),
            'ANDROID': None
        })

    @property
    def delete_ace(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, "Delete Ace"),
            'ANDROID': None
        })

    @property
    def hide_ace_from_feed(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, "Hide Ace From Feed"),
            'ANDROID': None
        })

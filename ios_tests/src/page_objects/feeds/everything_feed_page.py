from appium.webdriver.common.mobileby import MobileBy

from ios_tests.src.page_objects.feeds.base_feed import BaseFeed


class EverythingFeedPage(BaseFeed):
    def __init__(self):
        super().__init__(MobileBy.IOS_CLASS_CHAIN,
                         '**/XCUIElementTypeNavigationBar[`name == "Everything"`]', 'Everything Feed')


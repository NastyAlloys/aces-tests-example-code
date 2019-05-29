from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class HiddenAcesElements(BasePageElements):
    def __init__(self, ace_id=None):
        self.ace_id = ace_id

    @property
    def ace_by_id(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label BEGINSWITH "aces_feed_cell" and value BEGINSWITH "' +
                    str(self.ace_id) + '"'),
            'ANDROID': None
        })

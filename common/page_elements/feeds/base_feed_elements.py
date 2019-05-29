from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class BaseFeedElements(BasePageElements):
    def __init__(self, ace_id=None):
        self.ace_id = ace_id

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
    def sender_avatar(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'avatar_node'),
            'ANDROID': None
        })

    @property
    def ace_by_id(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label BEGINSWITH "aces_feed_cell" and value BEGINSWITH "' +
                    str(self.ace_id) + '"'),
            'ANDROID': None
        })

    @property
    def aces_feed_cell(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'aces_feed_cell'),
            'ANDROID': None
        })

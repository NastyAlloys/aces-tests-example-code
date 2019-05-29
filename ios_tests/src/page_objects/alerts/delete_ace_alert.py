from appium.webdriver.common.mobileby import MobileBy

from ..alerts.base_alert import BaseAlert
from caesar.mobile.elements.mobile_element import MobileElement


class DeleteAceAlert(BaseAlert):
    def __init__(self):
        super().__init__(MobileBy.IOS_PREDICATE, 'label BEGINSWITH "Delete Ace"',
                         "Delete Ace Alert")

    def click_delete(self):
        self.click_btn(self.page_elements.delete_btn)

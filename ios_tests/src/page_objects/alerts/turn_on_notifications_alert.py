from appium.webdriver.common.mobileby import MobileBy

from ..alerts.base_alert import BaseAlert
from caesar.mobile.elements.mobile_element import MobileElement


class TurnOnNotificationsAlert(BaseAlert):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID,
                         'To stay in the loop, please allow notifications.',
                         "Turn On Notification alert")
        self.yes_btn = MobileElement(MobileBy.ACCESSIBILITY_ID,
                                     "Yes")

    def click_yes(self):
        self.yes_btn.wait_clickable(False, self.w_alert)
        self.yes_btn.click()

from appium.webdriver.common.mobileby import MobileBy

from ..alerts.base_alert import BaseAlert
from caesar.mobile.elements.mobile_element import MobileElement


class AllowNotificationsAlert(BaseAlert):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID,
                         'Notifications may include alerts, sounds, and icon badges. These can be configured in Settings.',
                         "Allow Notification alert")
        self.allow_btn = MobileElement(MobileBy.ACCESSIBILITY_ID,
                                    "Allow")

    def click_allow(self):
        self.allow_btn.wait_clickable(False, self.w_alert)
        self.allow_btn.click()

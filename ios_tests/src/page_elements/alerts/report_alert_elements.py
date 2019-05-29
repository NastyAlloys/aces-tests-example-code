from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.alerts.base_alert_elements import BaseAlertElements


class ReportAlertElements(BaseAlertElements):
    @property
    def flip_reported_msg(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label BEGINSWITH "Flip Reported"'),
            'ANDROID': None
        })

    @property
    def ace_reported_msg(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label BEGINSWITH "Ace Reported"'),
            'ANDROID': None
        })


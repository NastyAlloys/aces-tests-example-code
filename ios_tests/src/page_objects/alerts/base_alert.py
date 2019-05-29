from caesar.common.logger import autolog
from caesar.mobile.elements.mobile_element import BaseElement

from common.page_objects.base_page import BasePage
from common.page_elements.alerts.base_alert_elements import BaseAlertElements


class BaseAlert(BasePage):
    def __init__(self, locator_type, locator, name):
        super().__init__(locator_type, locator, name)
        self.w_alert = 60
        self.page_elements = BaseAlertElements()

    def is_present(self):
        # assert page present, test fails if page is absent
        presence = BaseElement(self.locator_type,
                               self.locator, self.name).is_present()
        if presence:
            autolog("Alert '{0}' is present".format(self.name))
        else:
            autolog("Alert '{0}' is absent".format(self.name))
        return presence


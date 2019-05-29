from appium.webdriver.common.mobileby import MobileBy

from ..alerts.base_alert import BaseAlert
from ...page_elements.alerts.report_alert_elements import ReportAlertElements


class ReportAlert(BaseAlert):
    def __init__(self):
        super().__init__(MobileBy.IOS_PREDICATE, 'label BEGINSWITH "Report:"',
                         "Report alert")
        self.page_elements = ReportAlertElements()

    def fill_additional_info(self, text):
        self.click_btn(self.page_elements.text_field)
        self.input_text_in_element(self.page_elements.text_field, text)

    def click_send_btn(self):
        self.click_btn(self.page_elements.send_btn)

    def wait_for_done_btn(self):
        self.wait_presence_element(self.page_elements.done_btn)

    def click_done_btn(self):
        self.click_btn(self.page_elements.done_btn)

    def wait_for_message(self, is_flip_alert=True):
        if is_flip_alert:
            self.wait_presence_element(self.page_elements.flip_reported_msg)
        else:
            self.wait_presence_element(self.page_elements.ace_reported_msg)

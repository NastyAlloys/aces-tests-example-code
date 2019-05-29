import random

from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.user.push_notifications_page_elements import PushNotificationsPageElements


class PushNotificationsPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.IOS_CLASS_CHAIN,
                         '**/XCUIElementTypeNavigationBar[`name == "Push Notifications"`]', 'Push Notifications Page')
        self.page_elements = PushNotificationsPageElements()

    def switch_all_notifications(self, value="0"):
        self.wait_clickable_element(self.page_elements.turn_on_all_notif)
        self.toggle_switch_btn_with_value(self.page_elements.turn_on_all_notif, value)

    def wait_for_all_notifications(self, presence=True):
        random_notification = random.choice(self.page_elements.all_notifications)
        self.wait_presence_element(random_notification, 5, presence)

    def get_all_switches_value(self):
        all_switches_value = self.wait_presence_element(self.page_elements.all_switches,
                                                        5).wait_clickable().get_all_texts()
        return list(all_switches_value)

    def switch_random_notifications(self, count):
        random_elements = random.sample(self.page_elements.all_notifications, count)

        for i in random_elements:
            self.wait_presence_element(i, 5).wait_clickable().click()

    def is_all_notifications_on(self):
        return self.wait_presence_element(self.page_elements.turn_on_all_notif, 5).get_first_text() == "1"

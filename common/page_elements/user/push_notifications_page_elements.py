from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class PushNotificationsPageElements(BasePageElements):
    @property
    def turn_on_all_notif(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN,
                    '**/XCUIElementTypeSwitch[`name == "Turn On Push Notifications"`]'),
            'ANDROID': None
        })

    @property
    def received_an_ace_notif(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN,
                    '**/XCUIElementTypeSwitch[`name == "Received an Ace"`]'),
            'ANDROID': None
        })

    @property
    def added_by_user_notif(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN,
                    '**/XCUIElementTypeSwitch[`name == "Added by User"`]'),
            'ANDROID': None
        })

    @property
    def contact_joined_aces_notif(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN,
                    '**/XCUIElementTypeSwitch[`name == "Contact Joined Aces"`]'),
            'ANDROID': None
        })

    @property
    def other_recipient_reacted_notif(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN,
                    '**/XCUIElementTypeSwitch[`name == "Other Recipient Reacted"`]'),
            'ANDROID': None
        })

    @property
    def all_switches(self):
        return self._element({
            'IOS': (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch'),
            'ANDROID': None
        })

    @property
    def all_notifications(self):
        return [
            self.turn_on_all_notif,
            self.received_an_ace_notif,
            self.added_by_user_notif,
            self.contact_joined_aces_notif,
            self.other_recipient_reacted_notif
        ]

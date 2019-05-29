from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class AceDetailsElements(BasePageElements):
    def __init__(self, flip_id=None):
        self.flip_id = flip_id

    @property
    def share_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, '@'),
            'ANDROID': None
        })

    @property
    def add_reaction_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'add reaction'),
            'ANDROID': None
        })

    @property
    def view_flip_activity(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'View Flip Activity'),
            'ANDROID': None
        })

    @property
    def report_flip(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Report Flip'),
            'ANDROID': None
        })

    @property
    def report_ace(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Report Ace'),
            'ANDROID': None
        })

    @property
    def delete_ace(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Delete Ace'),
            'ANDROID': None
        })

    @property
    def delete_mutual_flip(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Delete This Flip'),
            'ANDROID': None
        })

    @property
    def delete_flip(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Delete Your Flip'),
            'ANDROID': None
        })

    @property
    def inappropriate_content(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Inappropriate content'),
            'ANDROID': None
        })

    @property
    def personal_information_disclosure(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Personal information disclosure'),
            'ANDROID': None
        })

    @property
    def offensive_behavior(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Offensive behavior'),
            'ANDROID': None
        })

    @property
    def other_tos_violation(self):
        return self._textbox_element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'Other Terms of Service violation'),
            'ANDROID': None
        })

    @property
    def user_reaction_cell(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'user_reaction_cell'),
            'ANDROID': None
        })

    @property
    def flip_by_id(self):
        return self._element({
            'IOS': (MobileBy.IOS_PREDICATE, 'label BEGINSWITH "user_reaction_cell" and value BEGINSWITH "' +
                    str(self.flip_id) + '"'),
            'ANDROID': None
        })

    @property
    def ace_owner_id(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'ace_owner_id'),
            'ANDROID': None
        })

    @property
    def reaction_owner(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'reaction_owner'),
            'ANDROID': None
        })

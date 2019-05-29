from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.base_page_elements import BasePageElements


class TutorialPageElements(BasePageElements):
    @property
    def tip_sheet_view(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, "ic_onbrd_background"),
            'ANDROID': None
        })

    @property
    def onbrd_flip_1(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, "ic_onbrd_flips_v2_1"),
            'ANDROID': None
        })

    @property
    def onbrd_flip_2(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, "ic_onbrd_flips_v2_2"),
            'ANDROID': None
        })

    @property
    def onbrd_flip_3(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, "ic_onbrd_flips_v2_3"),
            'ANDROID': None
        })

    @property
    def onbrd_flip_4(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, "ic_onbrd_flips_v2_4"),
            'ANDROID': None
        })

    @property
    def close_btn(self):
        return self._element({
            'IOS': (MobileBy.ACCESSIBILITY_ID, 'close small'),
            'ANDROID': None
        })

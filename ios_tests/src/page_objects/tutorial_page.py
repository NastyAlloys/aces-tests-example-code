from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.tutorial_page_elements import TutorialPageElements


class TutorialPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label BEGINSWITH "Video"`]',
                         'Tutorial Page')
        self.page_elements = TutorialPageElements()

    def walk_through(self):
        self.wait_presence_element(self.page_elements.close_btn)
        self.wait_presence_element(self.page_elements.onbrd_flip_1)
        self.swipe_right_to_left(coordinate_y=None, duration=100)
        self.wait_presence_element(self.page_elements.onbrd_flip_2)
        self.swipe_right_to_left(coordinate_y=None, duration=100)
        self.wait_presence_element(self.page_elements.onbrd_flip_3)
        self.swipe_right_to_left(coordinate_y=None, duration=100)
        self.wait_presence_element(self.page_elements.onbrd_flip_4)
        self.click_close_btn()

    def click_close_btn(self):
        self.click_btn(self.page_elements.close_btn)

import random

from appium.webdriver.common.mobileby import MobileBy

from common.page_elements.feeds.my_aces_elements import MyAcesElements
from ios_tests.src.page_objects.feeds.base_feed import BaseFeed


class MyAcesPage(BaseFeed):
    def __init__(self):
        super().__init__(MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar[`name == "My Aces"`]',
                         'My Aces Page')
        self.page_elements = MyAcesElements()

    def update_feed(self):
        content_cell_node = self.page_elements.content_cell_node
        self.wait_presence_element(content_cell_node)
        window_size = self.get_window_size()
        self.drag_by_coordinates(window_size["width"] / 2, window_size["height"] / 2,
                                 window_size["width"] / 2, window_size["height"])

        self.wait_pull_to_refresh_absent()

    def wait_for_created_ace(self):
        self.wait_presence_element(self.page_elements.ace_by_id)

    def long_tap_on_created_ace(self):
        self.page_elements.ace_by_id.wait_clickable()
        element_size = self.page_elements.ace_by_id.get_size()
        self.long_press_by_coordinates(element_size["x"] + element_size["width"] / 2,
                                       element_size["y"] + element_size["height"] / 2)

    def tap_on_created_ace(self):
        element_size = self.page_elements.ace_by_id.get_size()
        self.tap_by_coordinates(element_size["x"] + element_size["width"] / 2,
                                element_size["y"] + element_size["height"] / 2)

    def click_delete_ace(self):
        self.click_btn(self.page_elements.delete_ace)

    def click_hide_ace_from_feed(self):
        self.click_btn(self.page_elements.hide_ace_from_feed)

    def wait_created_ace_absent(self):
        self.wait_progress_hud_absent()
        self.wait_presence_element(self.page_elements.ace_by_id, 20, False)

    def is_ace_present(self):
        return self.page_elements.ace_by_id.is_present()

import random
from common.page_objects.base_page import BasePage

from common.page_elements.feeds.base_feed_elements import BaseFeedElements


class BaseFeed(BasePage):
    def __init__(self, locator_type, locator, name):
        super().__init__(locator_type, locator, name)
        self.page_elements = BaseFeedElements()

    def click_random_ace(self):
        self.wait_presence_element(self.page_elements.aces_feed_cell)
        aces_array = self.page_elements.aces_feed_cell.all_elements
        aces_array.pop(0)
        ace_to_click = random.choice(aces_array)

        ace_id = ace_to_click.get_attribute("value")
        self.page_elements.ace_id = ace_id
        self.click_ace_content(self.page_elements.ace_by_id)
        return ace_id

    def click_ace_details(self):
        self.wait_presence_element(self.page_elements.content_cell_node)
        content_node_size = self.page_elements.content_cell_node.get_size()
        header_node_size = self.page_elements.header_cell_node.get_size()

        self.tap_by_coordinates(content_node_size["x"],
                                content_node_size["y"] + header_node_size["height"])

    def click_random_ace_sender(self):
        self.wait_presence_element(self.page_elements.sender_avatar)
        aces_array = self.page_elements.sender_avatar.all_elements
        sender_to_click = random.choice(aces_array)
        sender_id = sender_to_click.get_attribute("value")
        sender_to_click.click()
        return sender_id

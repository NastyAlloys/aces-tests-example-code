import random

from appium.webdriver.common.mobileby import MobileBy

from common.page_objects.base_page import BasePage
from common.page_elements.view_ace.ace_details_elements import AceDetailsElements


class AceDetailsPage(BasePage):
    def __init__(self):
        super().__init__(MobileBy.ACCESSIBILITY_ID, 'add reaction', 'Ace Details Page')
        self.page_elements = AceDetailsElements()

    def click_ace_activity(self):
        self.click_btn(self.page_elements.menu_btn)
        self.click_btn(self.page_elements.view_flip_activity)

    def report_flip(self):
        self.click_btn(self.page_elements.menu_btn)
        self.click_btn(self.page_elements.report_flip)
        self.click_random_reason()

    def report_ace(self):
        self.click_btn(self.page_elements.menu_btn)
        self.click_btn(self.page_elements.report_ace)
        self.click_random_reason()

    def delete_ace(self):
        self.click_btn(self.page_elements.menu_btn)
        self.click_btn(self.page_elements.delete_ace)
        self.click_btn(self.page_elements.delete_btn)

    def click_random_reason(self):
        random_reason = self.get_random_reason()
        self.click_btn(random_reason)

    def get_random_reason(self):
        reasons_list = [
            self.page_elements.inappropriate_content,
            self.page_elements.offensive_behavior,
            self.page_elements.personal_information_disclosure,
            self.page_elements.other_tos_violation
        ]

        return random.choice(reasons_list)

    def update_flip_feed(self):
        user_reaction_cell = self.page_elements.user_reaction_cell
        self.wait_presence_element(user_reaction_cell)
        flip_size = user_reaction_cell.get_size()
        window_size = self.get_window_size()
        self.drag_by_coordinates(flip_size["x"], flip_size["y"],
                                 window_size["width"], flip_size["y"])
        self.wait_pull_to_refresh_absent()

    def wait_for_created_flip(self):
        self.wait_presence_element(self.page_elements.flip_by_id)

    def tap_on_created_flip(self):
        flip_size = self.page_elements.flip_by_id.get_size()
        self.tap_by_coordinates(flip_size["x"] + flip_size["width"] / 2,
                                flip_size["y"] + flip_size["height"] / 2)

    def is_flip_present(self):
        return self.page_elements.flip_by_id.is_present()

    def delete_flip(self, is_mutual=False):
        self.click_btn(self.page_elements.menu_btn)
        if is_mutual:
            self.click_btn(self.page_elements.delete_mutual_flip)
        else:
            self.click_btn(self.page_elements.delete_flip)
        self.click_btn(self.page_elements.delete_btn)
        self.wait_progress_hud_absent()
        self.wait_presence_element(self.page_elements.flip_by_id, None, False)

    def get_sender_uid(self):
        return self.page_elements.ace_owner_id.get_value()

    def long_press_random_flip(self):
        self.wait_presence_element(self.page_elements.reaction_owner)
        reaction_owner_array = self.page_elements.reaction_owner.all_elements
        reaction_owner_to_click = random.choice(reaction_owner_array)
        reaction_owner_id = reaction_owner_to_click.get_attribute("value")
        reaction_owner_rect = reaction_owner_to_click.rect

        self.long_press_driver_element(None, reaction_owner_rect["x"], reaction_owner_rect["y"])

        return reaction_owner_id


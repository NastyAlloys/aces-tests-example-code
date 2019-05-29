from random import randint

from caesar.mobile.mobile_page import MobilePage
from caesar.common.logger import autolog
from caesar.mobile.elements.mobile_element import MobileElement
from caesar.mobile.elements.mobile_text_box import MobileTextBox as TextBox

from common.page_elements.base_page_elements import BasePageElements


class BasePage(MobilePage):

    def __init__(self, locator_type, locator, name):
        super().__init__(locator_type, locator, name)
        self.page_elements = BasePageElements()

    def click_btn(self, element: MobileElement, wait_time=None):
        if wait_time:
            element.wait_element(wait_time).click()
        else:
            element.wait_element().click()

    def click_ace_content(self, element):
        element_size = element.get_size()
        self.tap_by_coordinates(element_size["x"] + element_size["width"] / 2,
                                element_size["y"] + element_size["height"] / 2)

    def wait_presence_element(self, element: MobileElement, wait_time=None, presence=True):
        if wait_time:
            if presence:
                element.wait_element(wait_time)
            else:
                element.wait_element_absent(wait_time)
        else:
            if presence:
                element.wait_element()
            else:
                element.wait_element_absent()
        return element

    def click_random_sibling_in_parent(self, parent_element: MobileElement):
        elements = self.wait_presence_element(parent_element).all_elements
        elements_len = len(elements)
        random_position = randint(0, elements_len - 1)
        elements[random_position].click()

    def input_text_in_element(self, element: TextBox, text, clear=True):
        element.wait_element()

        if clear:
            element.clear_text()
        element.type_text(text)

    def input_text_in_child_element(self, parent_element: MobileElement, child_position: MobileElement, text):
        parent_el = self.wait_presence_element(parent_element)

        child_field = parent_el.all_elements[child_position]
        child_field.click()
        child_field.send_keys(text)

    def is_element_present(self, element: MobileElement, wait_time=None, presence=True):
        if wait_time:
            if presence:
                return element.wait_element(wait_time).is_present()
            return not element.wait_element_absent(wait_time).is_present()
        else:
            if presence:
                return element.wait_element().is_present()
            return not element.wait_element_absent().is_present()

    def wait_clickable_element(self, element: MobileElement, wait_time=None):
        if wait_time:
            element.wait_clickable(wait_time)
        else:
            element.wait_clickable()
        return element

    def reverse_text_in_element(self, element: TextBox):
        element.wait_element()

        old_field_text = element.get_value()
        new_field_text = old_field_text[::-1]

        element.clear_text()
        element.type_text(new_field_text)

        return new_field_text

    def is_element_present_no_error(self, element: MobileElement, wait_time=5):
        element.wait_element_without_error(False, wait_time)
        return element.is_present()

    def wait_and_input_text_in_element(self, element: TextBox, text_to_wait, text_to_put, wait_time=15):
        element.wait_element()
        element.wait_text_presence_in_element(text_to_wait, wait_time)
        element.clear_text()
        element.type_text(text_to_put)

    def toggle_switch_btn_with_value(self, switch_btn: MobileElement, value):
        if switch_btn.get_value() != value:
            switch_btn.click()
            switch_btn.wait_text_presence_in_element_value(value)

    def select_from_options_dropdown_menu(self, select_element: MobileElement, choice_element: MobileElement,
                                          wait_time=5):
        self.wait_presence_element(select_element, wait_time)
        self.click_btn(select_element)
        self.wait_presence_element(choice_element, wait_time)
        self.click_btn(choice_element)

    def compare_element_value_with_text(self, element: MobileElement, text_to_compare):
        compare_element = element.wait_element_without_error(False, 5)
        autolog('Getting element to check value from')

        return compare_element.get_value() == text_to_compare

    def wait_progress_hud_absent(self):
        self.wait_presence_element(self.page_elements.progress_hud)
        self.wait_presence_element(self.page_elements.progress_hud, 5, False)

    def wait_pull_to_refresh_absent(self):
        self.wait_presence_element(self.page_elements.pull_to_refresh)
        self.wait_presence_element(self.page_elements.pull_to_refresh, 5, False)

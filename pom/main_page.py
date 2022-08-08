from base.base_object import BaseObject
from selenium.common.exceptions import NoSuchElementException
from locators.locators_list import IndexPageLocators as ind


class MainPageElements(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def find_hidden_element(self):
        self.is_hidden('css', ind.FIND_HIDDEN_ELEMENT_CSS).click()

    def find_clickable_element(self):
        self.is_visible('id', ind.FIND_CLICKABLE_ELEMENT_ID).click()

    def find_collapse_element(self):
        self.is_collapse('id', ind.FIND_COLLAPSE_ELEMENT_ID).click()

    def find_btn_add_to_cart(self):
        self.is_visible('id', ind.FIND_BTN_ADD_TO_CART_ID).click()

    def assert_cart_text(self):
        expected_text = 'Sauce Labs Backpack'
        actual_text = self.is_visible('id', ind.FIND_BACKPACK_ID).text
        assert actual_text == expected_text, f'Failed. Expected text is {expected_text}, but got {actual_text}'

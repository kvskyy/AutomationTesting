from base.base_object import BaseObject
from selenium.common.exceptions import NoSuchElementException
from locators.locators_list import IndexPageLocators as ind


class CartPageElements(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def find_checkout_btn(self):
        self.is_visible('id', ind.FIND_CHECKOUT_BTN_ID).click()

    def find_clickable_element(self):
        self.is_visible('id', ind.FIND_CLICKABLE_ELEMENT_ID).click()

    def assert_checkout_text(self):
        expected_text = 'CHECKOUT: YOUR INFORMATION'
        actual_text = self.is_visible('css', ind.FIND_CHECKOUT_CSS).text
        assert actual_text == expected_text, f'Failed. Expected text is {expected_text}, but got {actual_text}'


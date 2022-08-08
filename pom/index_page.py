from base.base_object import BaseObject
from selenium.common.exceptions import NoSuchElementException
from locators.locators_list import IndexPageLocators as ind


class Authorization(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_correct_username(self):
        self.is_visible('id', ind.FIND_USERNAME_FIELD_ID).send_keys('standard_user')

    def enter_locked_user(self):
        self.is_visible('id', ind.FIND_USERNAME_FIELD_ID).send_keys('locked_out_user')

    def enter_correct_password(self):
        self.is_visible('id', ind.FIND_PASSWORD_FIELD_ID).send_keys('secret_sauce')

    def click_login_button(self):
        self.is_visible('id', ind.FIND_LOGIN_BUTTON_ID).click()

    def perform_login(self):
        self.enter_correct_username()
        self.enter_correct_password()
        self.click_login_button()

    def setup_auth_assertion_text(self):
        expected_text = 'PRODUCTS'
        actual_text = self.is_visible('class', ind.FIND_PRODUCTS_TEXT_CLASS).text
        assert actual_text == expected_text, f'Failed. Expected text is {expected_text}, but got {actual_text}'

    def locked_assertion(self):
        lock_expected_text = 'Epic sadface: Sorry, this user has been locked out.'
        lock_actual_text = self.is_visible('css', ind.FIND_LOCKED_OUT_TEXT_CSS).text
        assert lock_actual_text == lock_expected_text, f'Failed. Expected text is {lock_expected_text}, but got ' \
                                                       f'{lock_actual_text}'

import pytest
import allure
from pom.cart_page import CartPageElements
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup_auth')
class TestCartPageElements:

    @pytest.mark.smoke
    @allure.description('Проверить checkout')
    @allure.label('owner', 'Oleg')
    @allure.severity(allure.severity_level.MINOR)
    def test_cart_page(self, get_webdriver):
        self.driver = get_webdriver
        step_cart = CartPageElements(get_webdriver)
        with allure.step('Открыть корзину'):
            step_cart.find_clickable_element()
        with allure.step('Выбрать проверку'):
            step_cart.find_checkout_btn()
        with allure.step('Получить результат'):
            step_cart.assert_checkout_text()

    @pytest.mark.ui
    def test_ui_scope(self):
        assert 1 == 1

    @pytest.mark.ui
    def test_user_i(self):
        assert 1 == 1

    @pytest.mark.ui
    def test_u_interface(self):
        assert 1 == 1

    @pytest.mark.ui
    def test_user_interface(self):
        assert 1 == 1

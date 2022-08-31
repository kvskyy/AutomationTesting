import pytest
import allure
from pom.main_page import MainPageElements
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup_auth')
class TestMainPageElements:

    @pytest.mark.smoke
    @allure.description('Проверка корзины')
    def test_add_to_cart(self, get_webdriver):
        self.driver = get_webdriver
        step_mp = MainPageElements(get_webdriver)
        with allure.step('Добавляем товар в корзину'):
            step_mp.find_btn_add_to_cart()
        step_mp.find_clickable_element()
        with allure.step('Получаем результат'):
            step_mp.assert_cart_text()

    '''def test_collapse_element(self):
        driver = self.driver
        step = MainPageElements(driver)
        step.find_collapse_element()
        
        '''

    @pytest.mark.smoke
    def test_smoke_1(self):
        assert 1 == 1

    @pytest.mark.smoke
    def test_smoke_2(self):
        assert 1 == 1

    @pytest.mark.smoke
    def test_smoke_3(self):
        assert 1 == 1

    @pytest.mark.smoke
    def test_smoke_4(self):
        assert 1 == 1

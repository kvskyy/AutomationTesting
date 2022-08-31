import pytest
import allure
from pom.index_page import Authorization


@pytest.mark.usefixtures('setup')
class TestAuthorization:

    @pytest.mark.smoke
    @allure.description('Правильный логин')
    def test_successful_login(self, get_webdriver):
        self.driver = get_webdriver
        step_auth = Authorization(get_webdriver)
        with allure.step('Вводим юзернейм'):
            step_auth.enter_correct_username()
        with allure.step('Вводим пароль'):
            step_auth.enter_correct_password()
        step_auth.click_login_button()
        with allure.step('Получаем результат'):
            step_auth.setup_auth_assertion_text()

    @allure.description('Заблокированный пользователь')
    def test_locked_out_user(self, get_webdriver):
        self.driver = get_webdriver
        step_lock = Authorization(get_webdriver)
        step_lock.enter_locked_user()
        step_lock.enter_correct_password()
        step_lock.click_login_button()
        step_lock.locked_assertion()

    @pytest.mark.sanity
    def test_sanity_up(self):
        assert 1 == 1

    @pytest.mark.sanity
    def test_sanity_down(self):
        assert 1 == 1

    @pytest.mark.sanity
    def test_sanity_left(self):
        assert 1 == 1

    @pytest.mark.sanity
    def test_sanity_right(self):
        assert 1 == 1

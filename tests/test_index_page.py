import pytest
from pom.index_page import Authorization


@pytest.mark.usefixtures('setup')
class TestAuthorization:

    @pytest.mark.smoke
    def test_successful_login(self, get_webdriver):
        self.driver = get_webdriver
        step_auth = Authorization(get_webdriver)
        step_auth.enter_correct_username()
        step_auth.enter_correct_password()
        step_auth.click_login_button()
        step_auth.setup_auth_assertion_text()

    def test_locked_out_user(self, get_webdriver):
        self.driver = get_webdriver
        step_lock = Authorization(get_webdriver)
        step_lock.enter_locked_user()
        step_lock.enter_correct_password()
        step_lock.click_login_button()
        step_lock.locked_assertion()



import pytest

from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage


@pytest.mark.usefixtures("get_driver")
class TestLogin:

    @pytest.mark.parametrize('login, password', [
        ('user_1', 'pass_1'),
        ('user_2', 'pass_2'),
        pytest.param('invalidData@gmail.com', 'invalidData', marks=pytest.mark.xfail)
    ])
    def test_login_valid(self, login, password):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.login()

        login_page = LoginPage(self.driver)
        login_page.wait_for_page_to_load()
        login_page.set_email(login)
        login_page.set_password(password)
        login_page.login()
        assert login_page.error_message_visible

        dashboard_page = DashboardPage(self.driver)
        dashboard_page.wait_for_page_to_load()
        assert dashboard_page.dropdown_visible

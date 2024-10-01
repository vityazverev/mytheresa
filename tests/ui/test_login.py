import pytest
from utilities.utils import perform_login


class TestLoginPage:

    @pytest.fixture
    def login_page_url(self, base_url):
        # Define the login page URL based on the base URL
        return f"{base_url}/login.html"

    def test_valid_login(self, page, login_page_url):
        user_name = 'demouser'
        user_pass = 'fashion123'

        perform_login(page, login_page_url, user_name, user_pass)

        welcome_message = page.locator("h2:text('Welcome, testUser!')")

        # Assert that the welcome message is visible
        assert welcome_message.is_visible()

    def test_invalid_login(self, page, login_page_url):
        user_name = 'demo'
        user_pass = 'demo'

        perform_login(page, login_page_url, user_name, user_pass)

        welcome_message = page.locator("div:text('Invalid username or password.')")

        assert welcome_message.is_visible()

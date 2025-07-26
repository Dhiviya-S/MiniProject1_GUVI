# Test Classes contains test scripts and calling actions
import pytest
# Importing Class LoginPage from login_page under Pages folder
from Pages.login_page import LoginPage
# To reuse data from Utils folder like valid credentials
from Utils.config import valid_email,valid_password


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestLogout:

    # test_successful_logout() enters valid data and clicks logout and moves back to login page again
    def test_successful_logout(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() from login_page.py and enters username and password
        login_page.login(valid_email,valid_password)

        # logout functionality and assert the homepage url after logout
        login_page.logout()
        print("Successful logout")
        assert "https://www.guvi.in" in login_page.get_current_url()
        print("Currently in login page:login_page.get_current_url()")



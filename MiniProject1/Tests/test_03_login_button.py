# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestLoginButton:

    #test_login_button() checks the visibility and clickability of the Login button.
    def test_login_button(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # Access the locator of LOGIN from LoginPage
        login_button=self.driver.find_element(*login_page.LOGIN_ICON)

        # is_displayed()checks the visibility
        assert login_button.is_displayed(), "Login button is not visible"
        # is_enabled() checks whether its clickable or not
        assert login_button.is_enabled(),"Login button is not clickable"

        # Navigates to login page
        login_page.click_login()
        print("Navigates to login page once clicked")


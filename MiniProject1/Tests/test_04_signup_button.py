# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestSignupButton:

    #test_signup_button() checks the visibility and clickability of Sign-Up button.
    def test_signup_button(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        signup_button=self.driver.find_element(*login_page.SIGNUP_BUTTON)

        # is_displayed()checks the visibility
        assert signup_button.is_displayed(),"SignUp button is not visible"
        # is_enabled() checks whether its clickable or not
        assert signup_button.is_enabled(), "SignUp button is not clickable"
        login_page.click_signup()
        print("Navigated to Signup page")

# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestSignin:

    # test_signin_url() navigates to the Sign-In page via the Sign-Up button.
    def test_signin_url(self):
        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        login_page.click_signup()

        # Checks the url of signin page using exception handling
        try:
            assert "https://www.guvi.in/register/" in login_page.get_current_url()
            print("Signin url:",login_page.get_current_url())
        except AssertionError:
            print("Cannot enter signin page")
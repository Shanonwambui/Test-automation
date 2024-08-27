import pytest
from src.pages.LoggedHomePage import LoggedHomePage
from src.tests.TestCase2 import TestCase2
from src.tests.test_home_page import TestHomePage
import allure

class TestCase4(TestHomePage):
    @allure.description("""
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter correct email address and password
        7. Click 'login' button
        8. Verify that 'Logged in as username' is visible
        9. Click 'Logout' button
        10. Verify that user is navigated to login page
    """)
    @pytest.mark.usefixtures("base_driver")
    def test_logout_user(self, base_driver):
        self.login_user_with_correct_email_and_password(base_driver)
        self.verify_that_user_is_logged_out(base_driver)
        

    def login_user_with_correct_email_and_password(self, base_driver):
        testcase2 = TestCase2()
        testcase2.verify_that_home_page_is_visible_successfully(base_driver)
        testcase2.verify_login_to_your_account_is_visible(base_driver)
        testcase2.verify_that_logged_in_as_username_is_visible(base_driver)

    def verify_that_user_is_logged_out(self, base_driver):
        logged_home_page = LoggedHomePage(base_driver)
        login_to_your_account_text  =logged_home_page.logout_button_click().get_login_to_your_account()
        assert login_to_your_account_text == "Login to your account", "Verify that user is navigated to login page"
   

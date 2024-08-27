# Python
import pytest
import allure
from src.pages.HomePage import HomePage
from src.pages.LoginSignupPage import LoginSignupPage
from src.utils.json_reader import existing_user
from src.tests.test_home_page import TestHomePage
from src.tests.TestCase1 import TestCase1
from src.utils.util import generate_current_date_and_time


class TestCase2(TestHomePage):
    @allure.description("""
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter correct email address and password
        7. Click 'login' button
        8. Verify that 'Logged in as username' is visible
        9. Click 'Delete Account' button
        10. Verify that 'ACCOUNT DELETED!' is visible""")
    @pytest.mark.usefixtures("base_driver")

    def test_login_user_with_correct_email_and_password(self,base_driver):
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_login_to_your_account_is_visible(base_driver)
        self.verify_that_logged_in_as_username_is_visible(base_driver)
        self.verify_that_account_deleted_is_visible_and_click_continue_button(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        # Assuming that you have a method in TestCase1 that verifies the home page is visible
        testcase1 = TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)

    def verify_login_to_your_account_is_visible(self, base_driver):
        login_to_your_account_text = HomePage(base_driver)
        assert login_to_your_account_text.signup_login_click().get_login_to_your_account() == "Login to your account", "Verify 'Login to your account' is visible"

    def verify_that_logged_in_as_username_is_visible(self, base_driver):
        username = LoginSignupPage(base_driver)
        assert username.fill_correct_login(existing_user("email"),existing_user("password")).get_username() == existing_user("name"), "Verify that 'Logged in as username' is visible"

    def verify_that_account_deleted_is_visible_and_click_continue_button(self,  base_driver):
        testcase1 = TestCase1()
        testcase1.verify_that_account_deleted_is_visible_and_click_continue_button(base_driver)
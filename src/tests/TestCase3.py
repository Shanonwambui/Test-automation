import pytest
import allure
from src.pages.LoginSignupPage import LoginSignupPage
from src.utils.util import generate_current_date_and_time
from src.tests.test_home_page import TestHomePage
from src.pages.LoginSignupPage import LoginSignupPage
from src.tests.TestCase2 import TestCase2

class TestCase3(TestHomePage):
    @allure.description("""
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter incorrect email address and password
        7. Click 'login' button
        8. Verify error 'Your email or password is incorrect!' is visible
    """)
    def test_login_user_with_incorrect_email_and_password(self, base_driver):
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_login_to_your_account_is_visible(base_driver)
        self.verify_error_your_email_or_password_is_incorrect_is_visible(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        testcase2 = TestCase2()
        testcase2.verify_that_home_page_is_visible_successfully(base_driver)

    def verify_login_to_your_account_is_visible(self, base_driver):
        TestCase2().verify_login_to_your_account_is_visible(base_driver)

    def verify_error_your_email_or_password_is_incorrect_is_visible(self, base_driver):
        email = "email" + generate_current_date_and_time() + "@gmail.com"
        password = "pass" + generate_current_date_and_time()

        login_signup_page = LoginSignupPage(base_driver)
        error_login_text = login_signup_page.fill_incorrect_login(email, password).get_error_login()
        assert error_login_text == "Your email or password is incorrect!", "Verify error 'Your email or password is incorrect!' is visible"
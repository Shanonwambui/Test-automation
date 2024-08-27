import pytest
from src.pages.LoginSignupPage import LoginSignupPage
from src.tests.TestCase1 import TestCase1
from src.tests.test_home_page import TestHomePage
import allure

class TestCase5(TestHomePage):
    @allure.description("""
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'New User Signup!' is visible
        6. Enter name and already registered email address
        7. Click 'Signup' button
        8. Verify error 'Email Address already exist!' is visible
    """)
    def test_register_user_with_existing_email(self, base_driver):
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_new_user_signup_is_visible(base_driver)
        self.verify_error_email_address_already_exist_is_visible(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        testcase1=TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)

    def verify_new_user_signup_is_visible(self, base_driver):
        TestCase1().verify_new_user_signup_is_visible(base_driver)

    def verify_error_email_address_already_exist_is_visible(self, base_driver):
        login_signup_page = LoginSignupPage(base_driver)
        email_address_already_exist_text = login_signup_page.fill_incorrect_signup().get_email_address_already_exist()
        assert email_address_already_exist_text == "Email Address already exist!", "Verify error 'Email Address already exist!' is visible"
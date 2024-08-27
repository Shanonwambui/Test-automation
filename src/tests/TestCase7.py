import pytest
import allure
from src.pages.HomePage import HomePage
from src.tests.TestCase1 import TestCase1
from src.tests.test_home_page import TestHomePage


class TestCase7(TestHomePage):

    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click on 'Test Cases' button
            5. Verify user is navigated to test cases page successfully""")
    def test_verify_test_cases_page(self, base_driver):
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_user_is_navigated_to_test_cases_page_successfully(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        testcase1 = TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)
    def verify_user_is_navigated_to_test_cases_page_successfully(self, base_driver):
        home_page = HomePage(base_driver)
        test_cases_text = home_page.test_cases_button_click().get_test_cases().text
        assert test_cases_text == "TEST CASES", "Verify user is navigated to test cases page successfully"
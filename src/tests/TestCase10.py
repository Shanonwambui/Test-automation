import pytest
import configparser
import allure
from src.pages.HomePage import HomePage
from src.tests.TestCase1 import TestCase1
from src.tests.test_home_page import TestHomePage
from src.tests.TestCase8 import TestCase8
from src.utils.properties_loader import load_property




class TestCase10(TestHomePage):

    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click on 'Products' button
            5. Verify user is navigated to ALL PRODUCTS page successfully
            6. Enter product name in search input and click search button
            7. Verify 'SEARCHED PRODUCTS' is visible
            8. Verify all the products related to search are visible""")
    def test_verify_subscription_in_home_page(self, base_driver):
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_text_subscription(base_driver)
        self.verify_success_message_you_have_been_successfully_subscribed_is_visible(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        testcase1 = TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)

    def verify_text_subscription(self, base_driver):
        subscription_text = HomePage(base_driver)
        assert subscription_text.get_subscription().text == "SUBSCRIPTION"

    def verify_success_message_you_have_been_successfully_subscribed_is_visible(self, base_driver):
        message_alert = HomePage(base_driver)
        assert message_alert.fill_subscribe().get_alert_success_subscribe() == "You have been successfully subscribed!"
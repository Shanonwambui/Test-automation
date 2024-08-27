# Python
import pytest
import allure
from src.pages.HomePage import HomePage
from src.pages.CartPage import CartPage
from src.tests.test_home_page import TestHomePage
from src.tests.TestCase1 import TestCase1
from src.tests.TestCase10 import TestCase10

class TestCase11(TestHomePage):

    @allure.epic("Regression Tests")
    @allure.feature("Cart")
    @allure.story("Verify Subscription in Cart page")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click 'Cart' button and scroll down to footer
            5. Verify text 'SUBSCRIPTION'
            6. Enter email address in input and click arrow button
            7. Verify success message 'You have been successfully subscribed!' is visible""")
    def test_verify_subscription_in_cart_page(self, base_driver):
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_cart_button_click(base_driver)
        self.verify_text_subscription(base_driver)
        self.verify_success_message_you_have_been_successfully_subscribed_is_visible(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        testcase1 = TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)
        
    def verify_cart_button_click(self, base_driver):
        home_page = HomePage(base_driver)
        home_page.cart_button_click()

    def verify_text_subscription(self, base_driver):
        subscription_text = CartPage(base_driver)
        assert subscription_text.get_subscription().text == "SUBSCRIPTION"

    def verify_success_message_you_have_been_successfully_subscribed_is_visible(self, base_driver):
        message_alert = CartPage(base_driver)
        assert message_alert.fill_subscribe().alert_success_subscribe() == "You have been successfully subscribed!"
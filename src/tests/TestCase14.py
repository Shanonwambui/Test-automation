# Python
import pytest
import allure
import json
from src.pages.HomePage import HomePage
from src.pages.ProductsPage import ProductsPage
from src.pages.AccountCreatedPage import AccountCreatedPage
from src.pages.LoggedHomePage import LoggedHomePage
from src.pages.CartPage import CartPage
from src.pages.CheckoutPage import CheckoutPage
from src.pages.LoginSignupPage import LoginSignupPage
from src.tests.test_home_page import TestHomePage
from src.tests.TestCase1 import TestCase1
from src.utils.util import generate_current_date_and_time
from src.utils.json_reader import account_details

class TestCase14(TestHomePage):
    name = "name" + generate_current_date_and_time()
    email = "email" + generate_current_date_and_time() + "@gmail.com"

    @allure.epic("Regression Tests")
    @allure.feature("Place Order")
    @allure.story("Place Order: Register while Checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Add products to cart
            5. Click 'Cart' button
            6. Verify that cart page is displayed
            7. Click Proceed To Checkout
            8. Click 'Register / Login' button
            9. Fill all details in Signup and create account
            10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
            11. Verify ' Logged in as username' at top
            12. Click 'Cart' button
            13. Click 'Proceed To Checkout' button
            14. Verify Address Details and Review Your Order
            15. Enter description in comment text area and click 'Place Order'
            16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
            17. Click 'Pay and Confirm Order' button
            18. Verify success message 'Congratulations! Your order has been confirmed!'
            19. Click 'Delete Account' button
            20. Verify 'ACCOUNT DELETED!' and click 'Continue' button""")
    def test_place_order_register_while_checkout(self, base_driver):
        # The methods called in this test are placeholders. Replace them with your actual methods.
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_that_cart_page_is_displayed(base_driver)
        self.verify_account_created_and_click_continue_button(base_driver)
        self.verify_logged_in_as_username_at_top(base_driver)
        self.verify_review_your_order(base_driver)
        self.verify_address_details(base_driver)
        self.verify_success_message_congratulations_your_order_has_been_confirmed(base_driver)
        self.verify_that_account_deleted_is_visible_and_click_continue_button(base_driver)

    def verify_that_home_page_is_visible_successfully(self,base_driver):
        testcase1 = TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)

    @allure.step("Verify that cart page is displayed")
    def verify_that_cart_page_is_displayed(self, base_driver):
        products = ProductsPage(base_driver)
        shopping_cart_text = products.add_products_to_cart().get_shopping_cart()
        assert shopping_cart_text == "Shopping Cart"
        home_page = CartPage(base_driver).get_proceed_to_checkout_button()


    @allure.step("Verify 'ACCOUNT CREATED!' and click 'Continue' button")
    def verify_account_created_and_click_continue_button(self, base_driver):
        home_page = HomePage(base_driver)
        account_created_text = home_page.signup_login_click().fill_correct_signup(self.name, self.email).fill_account_details().get_account_created().text
        assert account_created_text == "ACCOUNT CREATED!"
        account_created =  AccountCreatedPage(base_driver)
        account_created.continue_button_click()

    @allure.step("Verify ' Logged in as username' at top")
    def verify_logged_in_as_username_at_top(self, base_driver):
        logged_home = LoggedHomePage(base_driver)
        assert logged_home.get_username() == self.name, "Verify that 'Logged in as username' is visible"

    @allure.step("Verify Address Details and Review Your Order")
    def verify_review_your_order(self, base_driver):
        # The methods called in this step are placeholders. Replace them with your actual methods.
        cart = LoggedHomePage(base_driver).view_cart_click()
        product_names = cart.get_products_names()
        prices = cart.get_prices()
        quantity = cart.get_quantities()
        total_prices = cart.get_total_prices()
        check_out = CartPage(base_driver).proceed_to_checkout_logged_button_click()
        total_amount = check_out.get_total_amount().text
        

        for i in range(2):
            assert total_prices[i] == prices[i], "Verify Review Your Order"
            assert quantity[i] == "1", "Verify Review Your Order"
            assert product_names[0] == "Blue Top", "Verify Review Your Order"
            assert product_names[1] == "Sleeves Top and Short - Blue & Pink", "Verify Review Your Order"
            assert total_amount == "Rs. 978", "Verify Review Your Order"

        
    def verify_address_details(self, base_driver):
        """
        Verify the address details on the checkout page.

        Args:
            base_driver: The base driver object.

        Raises:
            AssertionError: If any of the address details do not match the expected values.
        """
        check_out=CheckoutPage(base_driver)
        address_delivery = check_out.get_address_delivery()
        address_invoice = check_out.get_address_invoice()

        assert address_delivery[0] == "YOUR DELIVERY ADDRESS", "Verify Address Details"
        assert address_invoice[0] == "YOUR BILLING ADDRESS", "Verify Address Details"

        for i in range(1, 8):
            assert address_delivery[i] == address_invoice[i], "Verify Address Details"

    
        no1 = "Mrs. " + account_details("firstName") + " " + account_details("lastName")
        no2 = account_details("company")
        no3 = account_details("address1")
        no4 = account_details("address2")
        no5 = account_details("city") + " " + account_details("state") + " " + account_details("zipcode")
        no6 = account_details("country")
        no7 = account_details("mobileNumber")

        assert address_delivery[1] == no1, "Verify Address Details"
        assert address_delivery[2] == no2, "Verify Address Details"
        assert address_delivery[3] == no3, "Verify Address Details"
        assert address_delivery[4] == no4, "Verify Address Details"
        assert address_delivery[5] == no5, "Verify Address Details"
        assert address_delivery[6] == no6, "Verify Address Details"
        assert address_delivery[7] == no7, "Verify Address Details"

    @allure.step("Verify success message 'Congratulations! Your order has been confirmed!'")
    def verify_success_message_congratulations_your_order_has_been_confirmed(self, base_driver):
        check_out=CheckoutPage(base_driver)
        alert_success_text = check_out.enter_comment("Sed fringilla aliquet turpis, ut vestibulum orci vulputate sit amet.").fill_payment_details().get_success_message()
        assert alert_success_text == "Congratulations! Your order has been confirmed!"

    @allure.step("Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button")
    def verify_that_account_deleted_is_visible_and_click_continue_button(self,base_driver):
        check_out = LoggedHomePage(base_driver)
        check_out.delete_account_button_click()

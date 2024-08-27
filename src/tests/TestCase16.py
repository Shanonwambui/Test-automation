import pytest
import allure

from src.pages.CartPage import CartPage
from src.tests.TestCase1 import TestCase1
from src.tests.test_home_page import TestHomePage
from src.tests.TestCase2 import TestCase2
from src.tests.TestCase14 import TestCase14
from src.pages.ProductsPage import ProductsPage
from src.pages.CheckoutPage import CheckoutPage


class TestCase16(TestHomePage):


    @pytest.mark.critical
    @pytest.mark.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click 'Signup / Login' button
            5. Fill email, password and click 'Login' button
            6. Verify 'Logged in as username' at top
            7. Add products to cart
            8. Click 'Cart' button
            9. Verify that cart page is displayed
            10. Click Proceed To Checkout
            11. Verify Address Details and Review Your Order
            12. Enter description in comment text area and click 'Place Order'
            13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
            14. Click 'Pay and Confirm Order' button
            15. Verify success message 'Congratulations! Your order has been confirmed!'""")
    def test_place_order_login_before_checkout(self, base_driver):
        TestCase1.verify_that_home_page_is_visible_successfully(self, base_driver)
        TestCase2.verify_login_to_your_account_is_visible(self, base_driver)
        TestCase2.verify_that_logged_in_as_username_is_visible(self, base_driver)
        self.verify_that_cart_page_is_displayed(base_driver)
        TestCase14.verify_review_your_order(self, base_driver)
        TestCase14.verify_address_details(self, base_driver)
        self.verify_success_message_congratulations_your_order_has_been_confirmed(base_driver)


    @allure.step("Verify that cart page is displayed")
    def verify_that_cart_page_is_displayed(self, base_driver):
        products = ProductsPage(base_driver)
        shopping_cart_text = products.add_products_to_cart().get_shopping_cart()
        assert shopping_cart_text == "Shopping Cart"
        home_page = CartPage(base_driver).get_proceed_to_checkout_button()

    def verify_success_message_congratulations_your_order_has_been_confirmed(self, base_driver):
        check_out=CheckoutPage(base_driver)
        alert_success_text = check_out.enter_comment("Sed fringilla aliquet turpis, ut vestibulum orci vulputate sit amet.").fill_payment_details().get_success_message()
        assert alert_success_text == "Congratulations! Your order has been confirmed!"

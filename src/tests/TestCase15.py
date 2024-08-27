import pytest
from src.pages.CartPage import CartPage
from src.tests.TestCase1 import TestCase1
from src.tests.TestCase14 import TestCase14
from src.utils.util import generate_current_date_and_time
from src.tests.test_home_page import TestHomePage
from src.pages.HomePage import HomePage
from src.pages.ProductsPage import ProductsPage

class TestCase15(TestHomePage):
    name = "name" + generate_current_date_and_time()
    email = "email" + generate_current_date_and_time() + "@gmail.com"

    @pytest.mark.critical
    def test_place_order_register_before_checkout(self, base_driver):
        TestCase1.verify_that_home_page_is_visible_successfully(self, base_driver)
        TestCase14.verify_account_created_and_click_continue_button(self, base_driver)
        TestCase14.verify_logged_in_as_username_at_top(self, base_driver)
        self.verify_that_cart_page_is_displayed(base_driver)
        TestCase14.verify_review_your_order(self, base_driver)
        TestCase14.verify_address_details(self, base_driver)
        TestCase14.verify_success_message_congratulations_your_order_has_been_confirmed(self, base_driver)
        TestCase1.verify_that_account_deleted_is_visible_and_click_continue_button(self, base_driver)

    def verify_that_cart_page_is_displayed(self, base_driver):
        products = ProductsPage(base_driver)
        shopping_cart_text = products.add_products_to_cart().get_shopping_cart()
        assert shopping_cart_text == "Shopping Cart"
        check_out = CartPage(base_driver).proceed_to_checkout_logged_button_click()

    
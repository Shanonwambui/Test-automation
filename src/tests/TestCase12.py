# Python
import pytest
import allure
from src.pages.HomePage import HomePage
from src.pages.CartPage import CartPage
from src.tests.test_home_page import TestHomePage
from src.tests.TestCase1 import TestCase1

class TestCase12(TestHomePage):
 
    @allure.epic("Regression Tests")
    @allure.feature("Cart")
    @allure.story("Add Products in Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click 'Products' button
            5. Hover over first product and click 'Add to cart'
            6. Click 'Continue Shopping' button
            7. Hover over second product and click 'Add to cart'
            8. Click 'View Cart' button
            9. Verify both products are added to Cart
            10. Verify their prices, quantity and total price""")

    def test_add_products_in_cart(self, base_driver):
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_both_products_are_added_to_cart(base_driver)
        self.verify_their_prices_quantity_and_total_price(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        testcase1 = TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)

    @allure.step("Verify both products are added to Cart")
    def verify_both_products_are_added_to_cart(self, base_driver):
        product_names = HomePage(base_driver).products_button_click().add_products_to_cart().get_products_names()
        assert len(product_names) == 2

    @allure.step("Verify their prices, quantity and total price")
    def verify_their_prices_quantity_and_total_price(self, base_driver):
        cart_page = CartPage(base_driver)
        prices = cart_page.get_prices()
        quantity = cart_page.get_quantities()
        total_prices = cart_page.get_total_prices()

        for i in range(2):
            assert total_prices[i] == prices[i]
            assert quantity[i] == "1"
            print(f"{i}. Prices = Total Prices | {prices[i]} = {total_prices[i]}")
            print(f"{i}. Quantity = 1 | {quantity[i] == '1'}")
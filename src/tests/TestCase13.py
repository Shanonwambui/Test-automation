# Python
import pytest
import allure
from src.pages.HomePage import HomePage
from src.pages.ProductDetailPage import ProductDetailPage
from src.tests.test_home_page import TestHomePage
from src.tests.TestCase1 import TestCase1

class TestCase13(TestHomePage):
   
    @allure.epic("Regression Tests")
    @allure.feature("Cart")
    @allure.story("Verify Product quantity in Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click 'View Product' for any product on home page
            5. Verify product detail is opened
            6. Increase quantity to 4
            7. Click 'Add to cart' button
            8. Click 'View Cart' button
            9. Verify that product is displayed in cart page with exact quantity""")
    def test_verify_product_quantity_in_cart(self, base_driver):
        self.verify_that_home_page_is_visible_successfully( base_driver)
        self.verify_product_detail_is_opened(base_driver)
        self.verify_that_product_is_displayed_in_cart_page_with_exact_quantity(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        testcase1 = TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)

    @allure.step("Verify product detail is opened")
    def verify_product_detail_is_opened(self, base_driver):
        home_page = HomePage(base_driver)
        home_page.view_product1_button_click()
        assert base_driver.title == "Automation Exercise - Product Details"

    @allure.step("Verify that product is displayed in cart page with exact quantity")
    def verify_that_product_is_displayed_in_cart_page_with_exact_quantity(self, base_driver):
        product_detail= ProductDetailPage(base_driver)
        quantity = product_detail.increase_quantity("4").add_to_cart_button_click().view_cart_button_click().get_quantities()
        assert quantity[0] == "4"
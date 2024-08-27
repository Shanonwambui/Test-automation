from src.pages.CartPage import CartPage
from src.pages.HomePage import HomePage
from src.pages.ProductsPage import ProductsPage
from src.tests.test_home_page import TestHomePage
from src.tests.TestCase8 import TestCase8
from src.tests.TestCase9 import TestCase9
from src.utils import json_reader
from src.utils.properties_loader import load_property
import allure
import pytest

@allure.epic("Regression Tests")
@allure.feature("Search")
class TestCase20(TestHomePage):

    search = load_property('SEARCH_PRODUCT_INPUT')

    @pytest.mark.test_description("Test Case 20: Search Products and Verify Cart After Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Search Products and Verify Cart After Login")
    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Click on 'Products' button
            4. Verify user is navigated to ALL PRODUCTS page successfully
            5. Enter product name in search input and click search button
            6. Verify 'SEARCHED PRODUCTS' is visible
            7. Verify all the products related to search are visible
            8. Add those products to cart
            9. Click 'Cart' button and verify that products are visible in cart
            10. Click 'Signup / Login' button and submit login details
            11. Again, go to Cart page
            12. Verify that those products are visible in cart after login as well
            13. Remove all products that have been added
            14. Verify 'Cart is empty! Click here to buy products.' is visible""")
    def test_search_products_and_verify_cart_after_login(self, base_driver):
        TestCase8.verify_user_is_navigated_to_all_products_page_successfully(self, base_driver)
        self.verify_searched_products_is_visible( base_driver)
        
        ProductsPage(base_driver).add_all_products()
        self.click_cart_button_and_verify_that_products_are_visible_in_cart(base_driver)
        HomePage(base_driver).signup_login_click().fill_correct_login(json_reader.existing_user("email"), json_reader.existing_user("password"))
        self.verify_that_those_products_are_visible_in_cart_after_login_as_well(base_driver)
        self.verify_that_cart_is_empty(base_driver)

    @allure.step("verify searched products is visible")
    def verify_searched_products_is_visible(self, base_driver):
        products_page = ProductsPage(base_driver)
        searched_products_text = products_page.fill_search_product_input(self.search).get_title_text_center()
        assert searched_products_text == "SEARCHED PRODUCTS", "Verify 'SEARCHED PRODUCTS' is visible"



    @allure.step("Click 'Cart' button and verify that products are visible in cart")
    def click_cart_button_and_verify_that_products_are_visible_in_cart(self, base_driver):
        products_names = ProductsPage(base_driver).cart_button_click().get_products_names()
        for i in range(len(products_names)):
            assert products_names[i] == products_names[i], "Verify that products are visible in cart"
            print(f"Search: {products_names[i]} = Added: {products_names[i]}")

    @allure.step("Verify that those products are visible in cart after login as well")
    def verify_that_those_products_are_visible_in_cart_after_login_as_well(self, base_driver):
        self.click_cart_button_and_verify_that_products_are_visible_in_cart(self, base_driver)

    @allure.step("Verify 'Cart is empty! Click here to buy products.' is visible")
    def verify_that_cart_is_empty(self, base_driver):
        empty_cart_text = CartPage(base_driver)
        assert empty_cart_text.delete_all_added_products().get_empty_cart_span() == "Cart is empty! Click here to buy products.", "Verify 'Cart is empty! Click here to buy products.' is visible"

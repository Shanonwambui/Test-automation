import pytest
import allure
from allure_commons.types import Severity
from src.pages.CartPage import CartPage
from src.tests.TestCase1 import TestCase1
from src.tests.TestCase16 import TestCase16
from src.tests.test_home_page import TestHomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



@pytest.mark.epic("Regression Tests")
@pytest.mark.feature("Cart")
class TestCase17(TestHomePage):

    @pytest.mark.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Add products to cart
            5. Click 'Cart' button
            6. Verify that cart page is displayed
            7. Click 'X' button corresponding to particular product
            8. Verify that product is removed from the cart""")
    @pytest.mark.severity(Severity.CRITICAL)
    
    def test_remove_products_from_cart(self, base_driver):
        TestCase1.verify_that_home_page_is_visible_successfully(self, base_driver)
        TestCase16.verify_that_cart_page_is_displayed(self, base_driver)
        self.verify_that_product_is_removed_from_the_cart(base_driver)

    @allure.step("Verify that product is removed from the cart")
    def verify_that_product_is_removed_from_the_cart(self, base_driver):
        CartPage(base_driver).x_button_click()
        WebDriverWait(base_driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@id='empty_cart']/p")))
        empty_cart_text = CartPage(base_driver).get_empty_cart_span()
        assert empty_cart_text == "Cart is empty! Click here to buy products.", "Verify that product is removed from the cart"
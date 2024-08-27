from src.pages.HomePage import HomePage
from src.pages.ProductsPage import ProductsPage
from src.utils import json_reader
from src.tests.test_home_page import TestHomePage
import allure
import pytest

@allure.epic("Regression Tests")
@allure.feature("Products")
class TestCase19(TestHomePage):
    @pytest.mark.test_description("Test Case 19: View & Cart Brand Products")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("View & Cart Brand Products")
    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Click on 'Products' button
            4. Verify that Brands are visible on left side bar
            5. Click on any brand name
            6. Verify that user is navigated to brand page and brand products are displayed
            7. On left side bar, click on any other brand link
            8. Verify that user is navigated to that brand page and can see products""")
    def test_view_cart_brand_products(self, base_driver):
        self.verify_that_brands_are_visible_on_left_sidebar(base_driver)
        self.verify_that_user_is_navigated_to_brand_page_and_brand_products_are_displayed(base_driver)
        self.verify_that_user_is_navigated_to_that_brand_page_and_can_see_products(base_driver)

    @allure.step("Verify that Brands are visible on left side bar")
    def verify_that_brands_are_visible_on_left_sidebar(self, base_driver):
        brands_is_displayed = HomePage(base_driver)
        assert brands_is_displayed.products_button_click().get_brands(), "Verify that Brands are visible on left side bar"

    @allure.step("Verify that user is navigated to brand page and brand products are displayed")
    def verify_that_user_is_navigated_to_brand_page_and_brand_products_are_displayed(self, base_driver):
        title_text_center = ProductsPage(base_driver)
        assert title_text_center.polo_brand_click().get_title_text_center() == "BRAND - POLO PRODUCTS", "Verify that user is navigated to brand page"

        products_names = ProductsPage(base_driver).get_products_search_names()
        for i, product_name in enumerate(products_names):
            assert product_name == json_reader.polo_brand_products(str(i)), "Verify that brand products are displayed"

    @allure.step("Verify that user is navigated to that brand page and can see products")
    def verify_that_user_is_navigated_to_that_brand_page_and_can_see_products(self,base_driver):
        title_text_center = ProductsPage(base_driver)
        assert title_text_center.madame_brand_click().get_title_text_center() == "BRAND - MADAME PRODUCTS", "Verify that user is navigated to that brand page"

        products_names = ProductsPage(base_driver).get_products_search_names()
        for i, product_name in enumerate(products_names):
            assert product_name == json_reader.madame_brand_products(str(i)), "Verify that can see products"

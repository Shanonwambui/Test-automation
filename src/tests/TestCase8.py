import pytest
import allure
from src.pages.HomePage import HomePage
from src.pages.ProductsPage import ProductsPage
from src.pages.ProductDetailPage import ProductDetailPage
from src.tests.test_home_page import TestHomePage
from src.tests.TestCase1 import TestCase1


class TestCase8(TestHomePage):

    
    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click on 'Products' button
            5. Verify user is navigated to ALL PRODUCTS page successfully
            6. The products list is visible
            7. Click on 'View Product' of first product
            8. User is landed to product detail page
            9. Verify that detail detail is visible: product name, category, price, availability, condition, brand""")
    def test_verify_all_products_and_product_detail_page(self, base_driver):
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_user_is_navigated_to_all_products_page_successfully(base_driver)
        ProductsPage(base_driver).view_product_of_first_product_button_click()
        self.verify_that_detail_detail_is_visible(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        testcase1 = TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)

    def verify_user_is_navigated_to_all_products_page_successfully(self, base_driver):
        home_page = HomePage(base_driver)
        all_products_text = home_page.products_button_click().get_title_text_center()
        assert all_products_text == "ALL PRODUCTS", "Verify user is navigated to ALL PRODUCTS page successfully"

    def verify_that_detail_detail_is_visible(self, base_driver):
        product_detail_page = ProductDetailPage(base_driver)
        assert product_detail_page.get_product_name(), "Verify that detail detail is visible: name"
        assert product_detail_page.get_product_category(), "Verify that detail detail is visible: category"
        assert product_detail_page.get_product_price(), "Verify that detail detail is visible: price"
        assert product_detail_page.get_product_availability(), "Verify that detail detail is visible: availability"
        assert product_detail_page.get_product_condition(), "Verify that detail detail is visible: condition"
        assert product_detail_page.get_product_brand(), "Verify that detail detail is visible: brand"

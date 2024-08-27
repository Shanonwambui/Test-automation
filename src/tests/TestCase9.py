import pytest
import configparser
import allure
from pages.ProductsPage import ProductsPage
from src.tests.TestCase1 import TestCase1
from src.tests.test_home_page import TestHomePage
from src.tests.TestCase8 import TestCase8
from src.utils.properties_loader import load_property



class TestCase9(TestHomePage):


    search = load_property('SEARCH_PRODUCT_INPUT')

    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click on 'Products' button
            5. Verify user is navigated to ALL PRODUCTS page successfully
            6. Enter product name in search input and click search button
            7. Verify 'SEARCHED PRODUCTS' is visible
            8. Verify all the products related to search are visible""")
    def test_search_product(self, base_driver):
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_user_is_navigated_to_all_products_page_successfully(base_driver)
        self.verify_searched_products_is_visible(base_driver)
        self.verify_all_the_products_related_to_search_are_visible(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        testcase1 = TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)

    def verify_user_is_navigated_to_all_products_page_successfully(self, base_driver):
        testcase8 = TestCase8()
        testcase8.verify_user_is_navigated_to_all_products_page_successfully(base_driver)
        
    def verify_searched_products_is_visible(self, base_driver):
        products_page = ProductsPage(base_driver)
        searched_products_text = products_page.fill_search_product_input(self.search).get_title_text_center()
        assert searched_products_text == "SEARCHED PRODUCTS", "Verify 'SEARCHED PRODUCTS' is visible"

    def verify_all_the_products_related_to_search_are_visible(self, base_driver):
        products_page = ProductsPage(base_driver)
        products_names = products_page.get_products_search_names()

        for i, product_name in enumerate(products_names):
            assert self.search.lower() in product_name.lower(), f"{i}. {product_name} - contain: {self.search}"
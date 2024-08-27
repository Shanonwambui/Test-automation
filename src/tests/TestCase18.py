import pytest
from selenium import webdriver
from src.pages.HomePage import HomePage
from src.pages.ProductsPage import ProductsPage
from src.tests.test_home_page import TestHomePage


@pytest.mark.regression

class TestCase18(TestHomePage):
    @pytest.mark.critical
    @pytest.mark.description(  """
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that categories are visible on left side bar
        4. Click on 'Women' category
        5. Click on any category link under 'Women' category, for example: Dress
        6. Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'
        7. On left side bar, click on any sub-category link of 'Men' category
        8. Verify that user is navigated to that category page
        """)
    def test_view_category_products(self,base_driver):
        self.verify_that_categories_are_visible_on_left_side_bar(base_driver)
        self.verify_that_category_page_is_displayed_and_confirm_text_women_dress_products(base_driver)
        self.verify_that_user_is_navigated_to_that_category_page(base_driver)

    def verify_that_categories_are_visible_on_left_side_bar(self, base_driver):
        categories_are_visible = HomePage(base_driver).get_categories().is_displayed()
        assert categories_are_visible, "Verify that categories are visible on left side bar"

    def verify_that_category_page_is_displayed_and_confirm_text_women_dress_products(self, base_driver):
        title_text_center = HomePage(base_driver).women_category_click().dress_category_click().get_title_text_center()
        assert title_text_center == "WOMEN - DRESS PRODUCTS", "Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'"

    def verify_that_user_is_navigated_to_that_category_page(self, base_driver):
        title_text_center = ProductsPage(base_driver).men_category_click().t_shirts_category_click().get_title_text_center()
        assert title_text_center == "MEN - TSHIRTS PRODUCTS", "Verify that user is navigated to that category page"
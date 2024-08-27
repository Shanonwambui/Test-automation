# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.ProductDetailPage import ProductDetailPage
from src.pages.CartPage import CartPage
from src.utils.selenium_helper import wait_for_element_to_be_clickable
import time
class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_title_text_center(self):
        time.sleep(5)
        title_text_center = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".title.text-center"))
        )
        return title_text_center.text

    def view_product_of_first_product_button_click(self):
        view_product_of_first_product_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/product_details/1']"))
        )
        view_product_of_first_product_button.click()
        return ProductDetailPage(self.driver)

    def fill_search_product_input(self, search_product):
        search_product_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_product"))
        )
        submit_search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "submit_search"))
        )
        search_product_input.send_keys(search_product)
        submit_search_input.click()
        return self

    def get_products_search_names(self):
        search_results_names = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'productinfo text-center')]//p"))
        )
        return [element.text for element in search_results_names]

    def add_products_to_cart(self):
        add_to_cart_button1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-product-id='1']"))
        )
        continue_shopping_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-dismiss='modal']"))
        )

        add_to_cart_button2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-product-id='16']"))
        )
        view_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/view_cart'] u"))
        )

        
        
        wait_for_element_to_be_clickable(self.driver, add_to_cart_button1)
        add_to_cart_button1.click()
        wait_for_element_to_be_clickable(self.driver, continue_shopping_button)
        continue_shopping_button.click()
        wait_for_element_to_be_clickable(self.driver, add_to_cart_button2)
        add_to_cart_button2.click()
        wait_for_element_to_be_clickable(self.driver, view_cart_button)
        view_cart_button.click()
        return CartPage(self.driver)

    def men_category_click(self):
        men_category = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='#Men']"))
        )
        men_category.click()
        return self

    def t_shirts_category_click(self):
        t_shirts_category = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category_products/3']"))
        )
        t_shirts_category.click()
        return self

    def get_brands(self):
        brands = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='brands-name']"))
        )
        return brands.text

    def polo_brand_click(self):
        time.sleep(5)
        polo_brand = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/brand_products/Polo']"))
        )
        polo_brand.click()
        return self

    def madame_brand_click(self):
        time.sleep(5)
        madame_brand = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/brand_products/Madame']"))
        )
        madame_brand.click()
        return self

    def add_all_products(self):
        add_buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='btn btn-default add-to-cart']"))
        )
        continue_shopping_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-dismiss='modal']"))
        )

        for i in range(0, len(add_buttons), 2):
            wait_for_element_to_be_clickable(self.driver, add_buttons[i])
            add_buttons[i].click()
            wait_for_element_to_be_clickable(self.driver, continue_shopping_button)
            continue_shopping_button.click()
        return self
    
    def cart_button_click(self):
        self.cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/view_cart']"))
        )
        self.cart_button.click()
        return CartPage(self.driver)

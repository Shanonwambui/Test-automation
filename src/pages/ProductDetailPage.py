# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.CartPage import CartPage
from src.utils.json_reader import existing_user
from src.utils.selenium_helper import wait_for_element_to_be_clickable

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='product-information'] h2"))
        )
        self.product_category = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section/div/div/div[2]/div[2]/div[2]/div/p[1]"))
        )
        self.product_price = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='product-information'] span span"))
        )
        self.product_availability = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section/div/div/div[2]/div[2]/div[2]/div/p[2]"))
        )
        self.product_condition = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section/div/div/div[2]/div[2]/div[2]/div/p[3]"))
        )
        self.product_brand = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section/div/div/div[2]/div[2]/div[2]/div/p[4]"))
        )
        self.quantity_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "quantity"))
        )
        self.add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='btn btn-default cart']"))
        )
        self.view_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/view_cart'] u"))
        )
        self.write_your_review = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='#reviews']"))
        )
        self.your_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        )
        self.email_address = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        self.add_review_here = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "review"))
        )
        self.submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "button-review"))
        )
        self.success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='alert-success alert'] span"))
        )

    def get_product_name(self):
        return self.product_name.text

    def get_product_category(self):
        return self.product_category.text

    def get_product_price(self):
        return self.product_price.text

    def get_product_availability(self):
        return self.product_availability.text

    def get_product_condition(self):
        return self.product_condition.text

    def get_product_brand(self):
        return self.product_brand.text

    def increase_quantity(self, value):
        self.quantity_input.clear()
        self.quantity_input.send_keys(value)
        return self

    def add_to_cart_button_click(self):
        self.add_to_cart_button.click()
        return self

    def view_cart_button_click(self):
        wait_for_element_to_be_clickable(self.driver, self.view_cart_button)
        self.view_cart_button.click()
        return CartPage(self.driver)

    def get_write_your_review(self):
        return self.write_your_review.text

    def fill_review(self):
        self.your_name_input.send_keys(existing_user("name"))
        self.email_address.send_keys(existing_user("email"))
        self.add_review_here.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit." +
                                       " Sed viverra, elit quis interdum feugiat, mi urna aliquam est, at venenatis quam odio et nisl." +
                                       " In at massa sit amet dui hendrerit mattis ac sit amet erat.")
        self.submit_button.click()
        return self

    def get_success_message(self):
        return self.success_message.text
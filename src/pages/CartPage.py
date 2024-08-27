# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.CheckoutPage import CheckoutPage
from src.pages.LoginSignupPage import LoginSignupPage
from src.utils.selenium_helper import wait_for_element_to_be_clickable

from src.utils.json_reader import existing_user
from src.utils.selenium_helper import wait_for_element_to_be_clickable

import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_home_button(self):
        home_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/']"))
        )
        wait_for_element_to_be_clickable(self.driver, home_button)
        home_button.click()
    def get_product_names(self):
        self.product_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//td[contains(@class, 'cart_description')]//a"))
        )
        return self.product_name
    
    def shopping_cart(self):
        self.shopping_cart = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li[class='active']"))
        )
        return self.shopping_cart
    def get_proceed_to_checkout_button(self):
        self.proceed_to_checkout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='btn btn-default check_out']"))
        )
        return self.proceed_to_checkout_button
    def register_login_button(self):
        self.register_login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/login'] u"))
        )
        return self.register_login_button
    def get_x_button_1(self):
        self.x_button_1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-product-id='1']"))
        )
        return self.x_button_1
    
    def get_x_button_2(self):
        self.x_button_2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-product-id='16']"))
        )
        return self.x_button_2
    
  
    def get_x_buttons(self):
        self.x_buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='cart_quantity_delete']"))
        )
        return self.x_buttons
    def get_subscription(self):
        self.subscription = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='single-widget'] h2"))
        )
        return self.subscription
    def get_subscribe_email_input(self):
        self.subscribe_email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "susbscribe_email"))
        )
        return self.subscribe_email_input
 
    def get_alert_success_subscribe(self):
        self.alert_success_subscribe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "success-subscribe"))
        )
        return self.alert_success_subscribe

    def get_products_names(self):
        product_name= self.get_product_names()
        return [element.text for element in self.product_name]

    def get_prices(self):
        self.price = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//td[contains(@class, 'cart_price')]/p"))
        )
        return [element.text for element in self.price]

    def get_quantities(self):
        self.quantity = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//td[contains(@class, 'cart_quantity')]/button"))
        )
        return [element.text for element in self.quantity]

    def get_total_prices(self):
        self.total_price = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//p[contains(@class, 'cart_total_price')]"))
        )
        return [element.text for element in self.total_price]


    def proceed_to_checkout_logged_button_click(self):
        self.get_proceed_to_checkout_button().click()
        return CheckoutPage(self.driver)

    def register_login_button_click(self):
        self.get_register_login_button().click()
        return LoginSignupPage(self.driver)

    def x_button_click(self):
        self.get_x_button_1().click()
        self.get_x_button_2().click()
        return self

    def get_shopping_cart(self):
        self.shopping_cart()
        return self.shopping_cart.text
    
    def get_empty_cart_span(self):
        self.empty_cart_span = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='empty_cart']/p"))
        )
        return self.empty_cart_span.text

    def delete_all_added_products(self):
        self.get_empty_cart_text()
        for button in self.x_buttons:
            button.click()
            time.sleep(0.5)
        return self
    
    def fill_subscribe(self):
        self.get_subscribe_email_input().send_keys(existing_user("email"))
        self.subscribe_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "subscribe"))
        )
        self.subscribe_button.click()
        return self

    def alert_success_subscribe(self):
        return self.get_alert_success_subscribe().text
    
    
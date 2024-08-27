# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.BasePage import BasePage
from src.pages.LoginSignupPage import LoginSignupPage
from src.pages.ProductsPage import ProductsPage
import time

from src.pages.ContactUsPage import ContactUsPage

from src.pages.CartPage import CartPage

from src.pages.ProductDetailPage import ProductDetailPage
from src.utils.json_reader import existing_user
from src.utils.selenium_helper import wait_for_element_to_be_clickable, wait_for_element_to_be_visible

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
        self.girl_img_responsive = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='item active'] img[alt='demo website for practice']"))
        )
        self.signup_login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/login']"))
        )
        self.contact_us_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/contact_us']"))
        )
        self.test_cases_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/test_cases']"))
        )
        self.products_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/products']"))
        )
        self.cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/view_cart']"))
        )
        self.view_product1_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/product_details/1']"))
        )
        # Python
        self.categories = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "accordian"))
        )
        self.women_category = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='accordian']/div[1]/div[1]/h4/a/span/i"))
        )
        self.dress_category = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category_products/1']"))
        )
        self.recommended_items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='recommended_items'] h2"))
        )
        self.blue_top_add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='recommended-item-carousel'] a[class='btn btn-default add-to-cart']"))
        )
        self.view_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='modal-content'] a[href='/view_cart']"))
        )
        # Python
        self.scroll_up_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "scrollUp"))
        )
        self.full_fledged_practice_website_for_automation_engineers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section[1]/div/div/div/div/div/div[1]/div[1]/h2"))
        )
        self.subscription = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='single-widget'] h2"))
        )
        self.subscribe_email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "susbscribe_email"))
        )
        self.subscribe_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "subscribe"))
        )
        self.alert_success_subscribe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "success-subscribe"))
        )
        
        # ... other elements ...

    def home_page_is_visible(self):
        return self.girl_img_responsive.is_displayed()

    def signup_login_click(self):
        self.signup_login_button.click()
        return LoginSignupPage(self.driver)
    
    def contact_us_button_click(self):
        self.contact_us_button.click()
        return ContactUsPage(self.driver)

    def test_cases_button_click(self):
        self.test_cases_button.click()
        return BasePage(self.driver)

    def products_button_click(self):
        self.products_button.click()
        return ProductsPage(self.driver)

    def cart_button_click(self):
        self.cart_button.click()
        return CartPage(self.driver)

    def view_product1_button_click(self):
        wait_for_element_to_be_clickable(self.driver, self.view_product1_button)
        self.view_product1_button.click()
        return ProductDetailPage(self.driver)

    def get_categories(self):
        return self.categories
    
    def women_category_click(self):
        wait_for_element_to_be_clickable(self.driver, self.women_category)
        self.women_category.click()
        return self

    def dress_category_click(self):
        wait_for_element_to_be_clickable(self.driver, self.dress_category)
        self.dress_category.click()
        return ProductsPage(self.driver)

    def get_recommended_items(self):
        return self.recommended_items

    def blue_top_add_to_cart_button_click(self):
        wait_for_element_to_be_clickable(self.driver, self.blue_top_add_to_cart_button)
        self.blue_top_add_to_cart_button.click()
        return self

    def view_cart_button_click(self):
        wait_for_element_to_be_visible(self.driver, self.view_cart_button)
        self.view_cart_button.click()
        return CartPage(self.driver)
    
    def scroll_up_button_click(self):
        self.scroll_up_button.click()
        return self

    def get_full_fledged_practice_website_for_automation_engineers(self):
        wait_for_element_to_be_visible(self.driver, self.full_fledged_practice_website_for_automation_engineers)
        return self.full_fledged_practice_website_for_automation_engineers

    def get_subscription(self):
        return self.subscription

    # ... other methods ...

    def fill_subscribe(self):
        self.subscribe_email_input.send_keys(existing_user("email"))
        wait_for_element_to_be_clickable(self.driver, self.subscribe_button)
        self.subscribe_button.click()
        return self

    def get_alert_success_subscribe(self):
        return self.alert_success_subscribe.text
    
    
# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utils.json_reader import payment_details
from src.utils.selenium_helper import wait_for_element_to_be_clickable

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_on_card_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='name-on-card']"))
        )
        self.card_number_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='card-number']"))
        )
        self.cvc_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='cvc']"))
        )
        self.expiration_month_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='expiry-month']"))
        )
        self.expiration_year_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='expiry-year']"))
        )
        self.pay_and_confirm_order_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-qa='pay-button']"))
        )
        
       
        

    def fill_payment_details(self):
        self.name_on_card_input.send_keys(payment_details("nameOnCard"))
        self.card_number_input.send_keys(payment_details("cardNumber"))
        self.cvc_input.send_keys(payment_details("cvc"))
        self.expiration_month_input.send_keys(payment_details("expirationMonth"))
        self.expiration_year_input.send_keys(payment_details("expirationYear"))
        self.pay_and_confirm_order_button.click()
        return self

    def get_success_message(self):
        self.success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='col-sm-9 col-sm-offset-1'] p"))
        )
        return self.success_message.text

    def download_invoice_button_click(self):
        self.download_invoice_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='btn btn-default check_out']"))
        )
        self.download_invoice_button.click()
        return self

    def continue_button_click(self):
        from src.pages.HomePage import HomePage
        self.continue_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-qa='continue-button']"))
        )
        wait_for_element_to_be_clickable(self.driver, self.continue_button)
        self.continue_button.click()
        return HomePage(self.driver)
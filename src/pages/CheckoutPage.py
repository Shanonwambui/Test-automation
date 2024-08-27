# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.PaymentPage import PaymentPage

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.address_delivery = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//ul[contains(@id, 'address_delivery')]//li"))
        )
        self.address_invoice = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//ul[contains(@id, 'address_invoice')]//li"))
        )
        self.total_amount = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section/div/div[5]/table/tbody/tr[3]/td[4]/p"))
        )
        self.comment = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='message']"))
        )
        self.place_order_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/payment']"))
        )

    def get_address_delivery(self):
        return [element.text for element in self.address_delivery]

    def get_address_invoice(self):
        return [element.text for element in self.address_invoice]

    def get_total_amount(self):
        return self.total_amount

    def enter_comment(self, text):
        self.comment.send_keys(text)
        self.place_order_button.click()
        return PaymentPage(self.driver)
# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.LoggedHomePage import LoggedHomePage
from src.utils.selenium_helper import wait_for_element_to_disappear
class AccountCreatedPage:
    def __init__(self, driver):
        self.driver = driver
        self.account_created = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2[data-qa='account-created']"))
        )
        self.continue_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-qa='continue-button']"))
        )

    def get_account_created(self):
        return self.account_created

    def continue_button_click(self):
         # Wait for the obstructing element to disappear
        wait_for_element_to_disappear(self.driver, (By.ID, 'aswift_1'))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']")))
        self.continue_button.click()
        return LoggedHomePage(self.driver)
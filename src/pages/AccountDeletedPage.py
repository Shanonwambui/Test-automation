# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountDeletedPage:
    def __init__(self, driver):
        self.driver = driver
        self.account_deleted = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2[data-qa='account-deleted']"))
        )
        self.continue_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-qa='continue-button']"))
        )

    def get_account_deleted(self):
        return self.account_deleted

    def continue_button_click(self):
        from src.pages.HomePage import HomePage
        self.continue_button.click()
        return HomePage(self.driver)
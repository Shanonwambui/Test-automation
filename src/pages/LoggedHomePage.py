# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.util import generate_current_date_and_time



class LoggedHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a/b"))
        )
        self.delete_account_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//header/div/div/div/div[2]/div/ul/li[5]/a"))
        )
        self.logout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//header/div/div/div/div[2]/div/ul/li[4]/a"))
        )
        self.view_cart = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//header/div/div/div/div[2]/div/ul/li[3]/a"))
        )

    def get_username(self):
        username_text = self.username.text
        return username_text 

    def delete_account_button_click(self):
        from src.pages.AccountDeletedPage import AccountDeletedPage
        self.delete_account_button.click()
        return AccountDeletedPage(self.driver)

    def logout_button_click(self):
        from src.pages.LoginSignupPage import LoginSignupPage
        self.logout_button.click()
        return LoginSignupPage(self.driver)
    
    def view_cart_click(self):
        from src.pages.CartPage import CartPage
        self.view_cart.click()
        return CartPage(self.driver)
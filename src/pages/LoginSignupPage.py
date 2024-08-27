# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from src.pages.EnterAccountInformationPage import EnterAccountInformationPage
from src.pages.LoggedHomePage import LoggedHomePage

from src.utils.json_reader import existing_user

class LoginSignupPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login_to_your_account(self):

        self.login_to_your_account = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='login-form'] h2"))
        )
    def login_email_input(self):
        self.login_email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-email']"))
        )
    def login_password_input(self):
        self.login_password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-password']"))
        )
    def login_button(self):
        self.login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-qa='login-button']"))
        )
    def error_login(self):
        self.error_login = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div[1]/div/form/p"))
        )
    def new_user_signup(self):
        self.new_user_signup = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='signup-form'] h2"))
        )
    def signup_name_input(self):
        self.signup_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='signup-name']"))
        )
    def signup_email_input(self):
        self.signup_email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='signup-email']"))
        )
    def signup_button(self):
        self.signup_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-qa='signup-button']"))
        )
    def email_address_already_exist(self):
        self.email_address_already_exist = WebDriverWait(self.driver, 150).until(
            EC.presence_of_element_located((By.XPATH, "//section/div/div/div[3]/div/form/p"))
        )

    def get_new_user_signup(self):
        self.new_user_signup()
        self.new_user_signup = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='signup-form'] h2"))
        )
        return self.new_user_signup.text
    
  
    def fill_signup(self, name, email):
        self.signup_email_input()
        self.signup_name_input()
        self.signup_button()
        self.signup_name_input.send_keys(name)
        self.signup_email_input.send_keys(email)
        self.signup_button.click()

    def fill_correct_signup(self, name, email):
        self.fill_signup(name, email)
        return EnterAccountInformationPage(self.driver)

    def fill_incorrect_signup(self):
        self.fill_signup(existing_user("name"), existing_user("email"))
        return self

    def get_login_to_your_account(self):
        self.login_to_your_account()
        return self.login_to_your_account.text

    def fill_login(self, email, password):
        self.login_password_input()
        self.login_email_input()
        self.login_button()
        self.login_email_input.send_keys(email)
        self.login_password_input.send_keys(password)
        self.login_button.click()

    def fill_correct_login(self, email, password):
        self.fill_login(email, password)
        return LoggedHomePage(self.driver)

    def fill_incorrect_login(self, email, password):
        self.fill_login(email, password)
        return self

    def get_error_login(self):
        self.error_login()
        return self.error_login.text

    def get_email_address_already_exist(self):
        self.email_address_already_exist()
        return self.email_address_already_exist.text
    
    
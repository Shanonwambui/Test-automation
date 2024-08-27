# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from src.pages.AccountCreatedPage import AccountCreatedPage
from src.utils.json_reader import account_details
from src.utils.util import generate_current_date_and_time
from selenium.webdriver.common.action_chains import ActionChains
from src.utils.selenium_helper import wait_for_element_to_exist


class EnterAccountInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.enter_account_information = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//b[contains(.,'Enter Account Information')]"))
        )
        self.title_mrs_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "id_gender2"))
        )
        self.password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        self.days_select = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "days"))
        )
        self.months_select = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "months"))
        )
        self.years_select = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "years"))
        )
        self.newsletter_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "newsletter"))
        )
        self.special_offers_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "optin"))
        )
        self.first_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "first_name"))
        )
        self.last_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "last_name"))
        )
        self.company_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "company"))
        )
        self.address1_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "address1"))
        )
        self.address2_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "address2"))
        )
        self.country_select = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "country"))
        )
        self.state_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "state"))
        )
        self.city_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "city"))
        )
        self.zipcode_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "zipcode"))
        )
        self.mobile_number_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "mobile_number"))
        )
        self.create_account_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-qa='create-account']"))
        )

    def get_enter_account_information(self):
        return self.enter_account_information

    def fill_account_details(self):
        password = "pass" + generate_current_date_and_time()
        self.title_mrs_checkbox.click()
        self.password_input.send_keys(password)
        # Wait for the days_select element to be clickable and then interact with it
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'days')))
        Select(self.days_select).select_by_value(account_details("day"))



        # Wait for the years_select element to be clickable and then interact with it
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'years')))
        Select(self.years_select).select_by_value(account_details("year"))


        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'newsletter')))
        self.newsletter_checkbox.click()
        self.special_offers_checkbox.click()
        self.first_name_input.send_keys(account_details("firstName"))
        self.last_name_input.send_keys(account_details("lastName"))
        self.company_input.send_keys(account_details("company"))
        self.address1_input.send_keys(account_details("address1"))
        self.address2_input.send_keys(account_details("address2"))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'country')))
        Select(self.country_select).select_by_value(account_details("country"))
        self.state_input.send_keys(account_details("state"))
        self.city_input.send_keys(account_details("city"))
        self.zipcode_input.send_keys(account_details("zipcode"))
        self.mobile_number_input.send_keys(account_details("mobileNumber"))
        self.create_account_button.click()
        return AccountCreatedPage(self.driver)
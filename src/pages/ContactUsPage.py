# Python
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver
    
    def get_in_touch(self):
        self.get_in_touch = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2.title:nth-child(2)"))
        )
    def get_name_input(self):
        self.name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        return self.name_input
    def get_email_input(self):
        self.email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        return self.email_input
    def get_subject_input(self):
        self.subject_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "subject"))
        )
        return self.subject_input
    def get_message_input(self):
        self.message_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        return self.message_input
    def get_upload_file_input(self):
        self.upload_file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "upload_file"))
        )
        return self.upload_file_input
    def get_submit_button(self):
        self.submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "submit"))
        )
        return self.submit_button
       
    def get_alert_success(self):
        self.alert_success = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".status.alert.alert-success"))
        )
        return self.alert_success
    def get_home_page_button(self):
        self.home_page_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='btn btn-success']"))
        )
        return self.home_page_button

    def get_get_in_touch(self):
        self.get_in_touch()
        return self.get_in_touch.text

    def fill_form(self):
        self.get_name_input().send_keys("shanon")
        self.get_email_input().send_keys("shanonwambui24@gmail.com")
        self.get_subject_input().send_keys("Test subject")
        self.get_message_input().send_keys("Hello there")
        self.get_upload_file_input().send_keys(os.getcwd() + "/src/resources/testData/sample.txt")
        return self

    def submit_button_click(self):
        submit_button = self.get_submit_button()
        self.driver.execute_script("arguments[0].click();", submit_button)
        return self

    def ok_button_click(self):
        alert = Alert(self.driver)
        alert.accept()
        return self

    def get_alert_success(self):
        self.alert_success = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".status.alert.alert-success"))
        )
        return self.alert_success.text

    def home_page_button_click(self):
        from src.pages.HomePage import HomePage
        self.get_home_page_button().click()
        return HomePage(self.driver)
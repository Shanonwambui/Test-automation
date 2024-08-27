# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.helpers import get_driver
from src.utils.config import BASE_URL
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
       


    def get_test_cases(self):
        self.test_cases = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2[class='title text-center'] b"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self.test_cases)
        )
        return self.test_cases
    
    

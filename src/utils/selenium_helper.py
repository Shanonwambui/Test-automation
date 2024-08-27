# Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import os
import random
from selenium import webdriver

def wait_for_element_to_exist(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

def wait_for_element_to_be_visible(driver, element, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of(element)
    )

def wait_for_not_to_empty_list(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        lambda x: len(driver.find_elements(*locator)) > 0
    )

def wait_for_element_to_be_clickable(driver, element, timeout=5):
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(element)
    )

def wait_for_element_to_disappear(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(locator)
    )

def take_screenshot(driver):
    screenshot = driver.get_screenshot_as_png()
    random_number = random.randint(1000, 9999)
    path = f"src/test/resources/screenshots/screenshot{random_number}.png"
    with open(path, 'wb') as file:
        file.write(screenshot)
    return path
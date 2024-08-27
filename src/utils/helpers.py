# Python
import os
import time
from selenium import webdriver
from src.utils.config import BROWSER
from src.utils.config import BASE_URL
from src.utils.properties_loader import load_property

'''def get_driver():
    if BROWSER == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser: " + BROWSER)'''


def get_driver():
    profile = webdriver.FirefoxProfile()
    ublock_origin_path = os.path.expanduser(load_property('UBLOCK_ORIGIN_PATH'))
    profile.add_extension(ublock_origin_path)
    driver = webdriver.Firefox()  # Adjust this function based on your WebDriver setup
    driver.get(BASE_URL)
    return driver

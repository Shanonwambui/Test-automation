# properties_loader.py
from utils.config import SEARCH_PRODUCT_INPUT, BASE_URL, BROWSER, DOWNLOAD_FOLDER_PATH, UBLOCK_ORIGIN_PATH

def load_property(property_name):
    properties = {
        'SEARCH_PRODUCT_INPUT': SEARCH_PRODUCT_INPUT,
        'BASE_URL': BASE_URL,
        'BROWSER': BROWSER,
        'DOWNLOAD_FOLDER_PATH': DOWNLOAD_FOLDER_PATH,
        'UBLOCK_ORIGIN_PATH': UBLOCK_ORIGIN_PATH
    }
    return properties.get(property_name)
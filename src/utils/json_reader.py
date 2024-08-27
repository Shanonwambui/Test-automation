# Python
import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def existing_user(data):
    existing_user = read_json_file('src/resources/testData/ExistingUser.json')
    return existing_user.get(data)

def account_details(data):
    account_details = read_json_file('src/resources/testData/AccountDetails.json')
    return account_details.get(data)

def payment_details(data):
    payment_details = read_json_file('src/resources/testData/PaymentDetails.json')
    return payment_details.get(data)

def polo_brand_products(data):
    polo_brand_products = read_json_file('src/resources/testData/PoloBrandProducts.json')
    return polo_brand_products.get(data)

def madame_brand_products(data):
    madame_brand_products = read_json_file('src/resources/testData/MadameBrandProducts.json')
    return madame_brand_products.get(data)
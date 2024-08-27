import pytest
from allure_commons.types import Severity
import allure
from datetime import datetime
from src.pages import HomePage, LoginSignupPage, EnterAccountInformationPage, AccountCreatedPage, LoggedHomePage, AccountDeletedPage
from src.pages.EnterAccountInformationPage import EnterAccountInformationPage
from src.tests.test_home_page import TestHomePage
from src.pages.HomePage import HomePage
from src.pages.AccountCreatedPage import AccountCreatedPage
from src.pages.AccountDeletedPage import AccountDeletedPage
from src.pages.LoggedHomePage import LoggedHomePage
from src.utils.util import generate_current_date_and_time


class TestCase1(TestHomePage):
   
    # Use the timestamp when setting the name attribute
    name = "shanon" + generate_current_date_and_time()
    email = "email" + datetime.now().strftime("%Y%m%d%H%M%S") + "@gmail.com"

    @allure.epic("Regression Tests")
    @allure.feature("User")
    @allure.story("Register User")
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click on 'Signup / Login' button
            5. Verify 'New User Signup!' is visible
            6. Enter name and email address
            7. Click 'Signup' button
            8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
            9. Fill details: Title, Name, Email, Password, Date of birth
            10. Select checkbox 'Sign up for our newsletter!'
            11. Select checkbox 'Receive special offers from our partners!'
            12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
            13. Click 'Create Account button'
            14. Verify that 'ACCOUNT CREATED!' is visible
            15. Click 'Continue' button
            16. Verify that 'Logged in as username' is visible
            17. Click 'Delete Account' button
            18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button""")
    @pytest.mark.usefixtures("base_driver")
    

    def test_register_user(self, base_driver):
        self.verify_that_home_page_is_visible_successfully( base_driver)
        self.verify_new_user_signup_is_visible( base_driver)
        self.verify_that_enter_account_information_is_visible( base_driver)
        self.verify_that_account_created_is_visible(base_driver)
        self.verify_that_logged_in_as_username_is_visible(base_driver)
        self.verify_that_account_deleted_is_visible_and_click_continue_button(base_driver)

    @allure.step("Verify that home page is visible successfully")
    def verify_that_home_page_is_visible_successfully(self,base_driver):
        home_page_visible = HomePage(base_driver).home_page_is_visible()
        assert home_page_visible, "Verify that home page is visible successfully"

    @allure.step("Verify 'New User Signup!' is visible")
    def verify_new_user_signup_is_visible(self, base_driver):
        home_page = HomePage(base_driver)
        assert home_page.signup_login_click().get_new_user_signup() == "New User Signup!", "Verify 'New User Signup!' is visible"

    @allure.step("Verify that 'ENTER ACCOUNT INFORMATION' is visible")
    def verify_that_enter_account_information_is_visible(self, base_driver):
        enter_account_info_page = EnterAccountInformationPage(base_driver)
        enter_account_information_text = enter_account_info_page.get_enter_account_information().text
        assert enter_account_information_text == "ENTER ACCOUNT INFORMATION", "Verify that 'ENTER ACCOUNT INFORMATION' is visible"  

    @allure.step("Verify that 'ACCOUNT CREATED!' is visible")
    def verify_that_account_created_is_visible(self,    base_driver):
        enter_account_information_page = EnterAccountInformationPage(base_driver)
        assert enter_account_information_page.fill_account_details().get_account_created().text == "ACCOUNT CREATED!", "Verify that 'ACCOUNT CREATED!' is visible"

    @allure.step("Verify that 'Logged in as username' is visible")
    def verify_that_logged_in_as_username_is_visible(self,  base_driver):
        account_created_page = AccountCreatedPage(base_driver)
        assert account_created_page.continue_button_click().get_username() == self.name, "Verify that 'Logged in as username' is visible"

    @allure.step("Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button")
    def verify_that_account_deleted_is_visible_and_click_continue_button(self,  base_driver):
        logged_home_page = LoggedHomePage(base_driver)
        assert logged_home_page.delete_account_button_click().get_account_deleted().text == "ACCOUNT DELETED!", "Verify that 'ACCOUNT DELETED!' is visible"
        AccountDeletedPage(base_driver).continue_button_click()
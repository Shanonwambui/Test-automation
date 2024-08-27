import pytest
import allure
from src.pages.HomePage import HomePage
from src.pages.ContactUsPage import ContactUsPage
from src.tests.TestCase1 import TestCase1
from src.tests.test_home_page import TestHomePage

class TestCase6(TestHomePage):
    @allure.description("""
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Contact Us' button
        5. Verify 'GET IN TOUCH' is visible
        6. Enter name, email, subject and message
        7. Upload file
        8. Click 'Submit' button
        9. Click OK button
        10. Verify success message 'Success! Your details have been submitted successfully.' is visible
        11. Click 'Home' button and verify that landed to home page successfully
    """)
    def test_contact_us_form(self, base_driver):
        self.verify_that_home_page_is_visible_successfully(base_driver)
        self.verify_get_in_touch_is_visible(base_driver)
        self.verify_success_message_success_your_details_have_been_submitted_successfully_is_visible(base_driver)
        self.click_home_button_and_verify_that_landed_to_home_page_successfully(base_driver)

    def verify_that_home_page_is_visible_successfully(self, base_driver):
        testcase1 = TestCase1()
        testcase1.verify_that_home_page_is_visible_successfully(base_driver)

    def verify_get_in_touch_is_visible(self, base_driver):
        home_page = HomePage(base_driver)
        assert home_page.contact_us_button_click().get_get_in_touch()== "GET IN TOUCH", "Verify 'GET IN TOUCH' is visible"
          

    def verify_success_message_success_your_details_have_been_submitted_successfully_is_visible(self, base_driver):
        contact_us_page = ContactUsPage(base_driver)
        alert_success_text = contact_us_page.fill_form().submit_button_click().ok_button_click().get_alert_success()
        assert alert_success_text == "Success! Your details have been submitted successfully.", "Verify success message 'Success! Your details have been submitted successfully.' is visible"

    def click_home_button_and_verify_that_landed_to_home_page_successfully(self, base_driver):
        contact_us_page = ContactUsPage(base_driver)
        home_page_visible = contact_us_page.home_page_button_click().home_page_is_visible()
        assert home_page_visible, "Click 'Home' button and verify that landed to home page successfully"
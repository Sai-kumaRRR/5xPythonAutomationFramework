# Dashboard Page Class

# Page Locators
# Page Actions

import test.Utils.Commom_Utils import Webdriver_wait

from selenium.webdriver.common.by import By


class FreeTrialPage:

    def __init__(self, driver):
        self.driver = driver

    username_email_ft = (By.XPATH, "//span[@data-qa='lufexuloga']")
    button_click_ft = (By.XPATH, "//button[normalizespace()='Create a free trial account']")
    checkbox_terms = (By.XPATH, "//input[@id='page-756cupr-consent-checkbox']")

    def get_username_ft(self):
        return self.driver.find_element(*FreeTrialPage.username_email_ft)

    def get_button_click_ft(self):
        return self.driver.find_element(*FreeTrialPage.button_click_ft)

    def get_checkbox_terms(self):
        return self.driver.find_element(*FreeTrialPage.checkbox_terms)

    def get_error_msg_invalid_email(self):
        return self.driver.find_element(*FreeTrialPage.error_msg_invalid_email)

    def get_error_message_text(self):
        return self.get_error_msg_invalid_email().text

    def enter_free_trial_details_invalid(self, invalid_email):
        try:
            self.get_username_ft().send_keys(invalid_email)
            self.get_button_checkbox_terms().click()
            self.get_button_click_ft().click()

        except    Exception as e:
            print(e)

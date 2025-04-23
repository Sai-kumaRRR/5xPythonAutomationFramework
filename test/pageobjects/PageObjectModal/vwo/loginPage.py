# Login page
import time

# page Locator
# Page Actions

from selenium.webdriver.common.by import By
from test.Utils.common_Utils import webdriver_wait


class LoginPage:



    def __init__(self, driver):
        self.driver = driver

        # Page Locators

        username = (By.ID, "login-username")
        password = (By.NAME, "password")
        submit_button = (By.XPATH, "//button[@id='js-login-btn']")
        error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")

        # Remove them if you are not using them as of now
     free_trial = (By.XPATH , "//a[normalize-space()='start a free trial']")
        # forgot_password_button = (By.XPATH, "//.XPATH, "//button[normalize-space()='Forgot password']")
        # sso_login = (By.XPATH, "//button[normalize-space()='sign in using sso']")
        # remember_checkbox = (By.XPATH, "//label[@for='checkbox-remember']//span[@class=

        # page actions

    def get_username(self):
            return self.driver.find_element(*LoginPage.username)

    def get_password(self):
            return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
            return self.driver.find_element(*LoginPage.submit_button())

    def get_free_trail_button(self):
        return self.driver.find_element(*LoginPage.get_free_trail_button)


    def get_error_message(self):
            webdriver_wait(driver=self.driver, element_tuple=self.error_message, timeout=5)
            return self.driver.find_element(*LoginPage.error_message)

    def login_to_vwo(self, usr, pwd):
            try:
                self.get_username().send_keys(usr)
                self.get_username().send_keys(pwd)
                self.get_submit_button().click()
            except Exception as e:
                print(e)

    def free_trial_button_click(self):
        try:
            self.get_free_trial_button().click()
        except Exception as e:
            print(e)


    def get_error_message_text(self):
                    return self.get_error_message().text

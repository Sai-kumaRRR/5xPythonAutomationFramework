# Dashboard Page Class

# Page Locators
# Page Actions

import test.Utils.commom_Utils
import webdriver_wait
from selenium.webdriver.common.by import By


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

        user_logged_in = (By.XPATH, "////span[@data-qa='lufexuloga']")

        def get_user_logged_in(self):
            return self.driver.find_element(*DashboardPage.user_logged_in)

        def user_logged_in_text(self):
            webdriver_wait(driver=self.driver, element_tuple=self.user_logged_in, timeout=5)
            return self.get_user_logged_in().text

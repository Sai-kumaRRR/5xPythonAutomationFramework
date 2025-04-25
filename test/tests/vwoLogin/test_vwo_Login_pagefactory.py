import logging
import time
import selenium
from selenium import webdriver
from allure_commons.types import AttachmentType
from test.pageObjects.pageFactory.loginPage_PageFactory import LoginPage
from test.pageObjects.pageFactory.loginPage_DashboardFactory import DashboardPage

import allure
import pytest
from constants import Constants

@allure.epic("VWO App")
@allure.feature("Login Test")
class TestVWOLogin:

    @pytest.mark.usefixture("setup")
    @pytest.mark.qa
    def test_vwo_login_negative(self, setup):
        try:
            Logger = logging.getLogger(__name__)
            driver = setup
            driver.get(Constants.app_url())
            loginPage = LoginPage(driver)
            loginPage.login_to_vwo(usr=self.username, pwd=123)

        error_msg_element = loginPage.error_msg()
        assert error_msg_element == "Your email, password , IP address or location did not match"
        except Exception as e:
            print(e)



    def test_vwo_login_positive(self, setup):
        driver = setup
        driver.get(Constants.app_url())
        login_page = LoginPage(driver)
        login_page.login_to_vwo(user=self.username, pwd=self.password)
        dashboard_page = DashboardPage(driver)
        username = dashboard_page.user_logged_in_text()
        assert "AMAN" == username

        @pytest.mark.usefixture("setup")
        @pytest.mark.qa
        def test_vwo_login_negative_tc2(self, setup):
            pass
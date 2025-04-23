import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from test.constants.constants import Constants
from test.pageObjects.pageObjectModel.vwo.loginPage import loginPage
from test.pageobjects.pageObjectModel.vwo.dashboardPage import DashboardPage

from test.Utils.Utils import *


# Assertions and use the page object class
# Webdriver Start
# User Interaction + Assertions
# Close Webdriver


@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver


@allure.title("VWO Login Test")
@allure.description("TC0 - VWO App Negative Test")
@allure.feature("Feature |VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup
    login_page = LoginPage(driver=driver)
    login_page.login_to_vwo(usr=os.getenv("INVALID_USERNAME"), pwd=os.getenv("INVALID_PASSWORD"))
    error_msg_element = login_page.get_error_message_text()
    take_screen_shot(driver=driver, name="test_vwo_login_negative")
    assert error_msg_element == os.getenv("error_message_expected")


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup
    login_page = LoginPage(driver=driver)
    login_page.login_to_vwo(usr=os.getenv("USERNAME"), pwd=os.getenv("PASSWORD"))
    dashboard_Page = DashboardPage(driver=driver)
    take_screen_shot(driver=driver, name="test_vwo_login_psitive")
    assert os.getenv("USERNAME_LOGGED_IN") in dashboard_Page.user_logged_in_text()

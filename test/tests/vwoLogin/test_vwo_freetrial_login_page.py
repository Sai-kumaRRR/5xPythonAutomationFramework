import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from test.constants.constants import Constants
from test.pageObjects.pageObjectModel.vwo.loginPage import LoginPage
from test.pageobjects.pageObjectModel.vwo.freetrailPage import freetrailPage

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


@allure.title("VWO Free trial")
@allure.description("TC0 - VWO free trial")
@allure.feature("Feature |VWO free trial")
@pytest.mark.negative
def test_vwo_ft_negative(setup):
    driver = setup
    login_page = LoginPage(driver=driver)
    login_page.free_trial_button_click()
    take_screen_shot(driver=driver, name="test_vwo_ft_negative")
    free_trial_page = freetrailPage(driver=driver)
    free_trial_page.enter_free_trial_details_invalid("admin")
    error_msg_text = free_trial_page.get_error_message_text()
    assert error_msg_text == "The email address you entered in incorrect"



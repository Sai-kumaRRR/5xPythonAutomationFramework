import allure
import pytest
import time

from selenium import webdriver

@allure.title("Dry run of the framework  1")
@allure.description("Verify that Dry run is working 1")
@allure.feature("TC#0 - sample Test run")
@pytest.mark.sample
def test_sample_pass():
    print("Hello World")
    assert True == True


@allure.title("Dry run of the framework 2")
@allure.description("Verify that Dry run is working 2")
@allure.feature("TC#2 - sample Failed run")
@pytest.mark.sample
def test_sample_fail():
    print("Hello World")
    assert True == False

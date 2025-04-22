- web automation framework with POM in Python(Selenium)
# Tech stack
Python , Pytest
Selenium
Allure report

Gitignore , Pytest Report

- Page object model and page factory both
- highlight element while run
- parallel run with xdist
- my sql data base connect to verify data.
#all the dependencies used
pip install allure-pytest selenium
- pip install pytest selenium pytest-html openpyxl
- pip install selenium-page-factory
- pip install pyyaml faker openpyxl
- pip install mysql-connector-python
- pip install pytest-reportportal
- pip install python-dotenv

### how to run the framework?
pytest-n auto tests/vwoLoginTests/pom/test_*

### how to run testcase parallel?
pytest -n auto tests/test/vwo_login_Tests/test_vwo_login
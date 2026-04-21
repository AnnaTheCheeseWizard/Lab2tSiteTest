import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Edge(options=options)
    yield driver
    driver.quit()
import pytest
import configparser
from selenium import webdriver

config = configparser.ConfigParser()
config.read('config.conf')

@pytest.fixture
def driver():
    browser = config.get("Preferences", "BROWSER").lower()
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Browser is not supported: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()

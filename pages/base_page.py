from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def is_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0
    
    def click(self, locator):
        self.wait_for_element(locator).click()

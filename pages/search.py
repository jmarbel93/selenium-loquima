from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Search(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")
    
    def search(self, query):
        self.wait_for_element(self.search_box).send_keys(query)
        self.wait_for_element(self.search_button).click()

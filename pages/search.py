from selenium.webdriver.common.by import By

class Search:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")

    def search(self, query):
        self.driver.find_element(*self.search_box).send_keys(query)
        self.driver.find_element(*self.search_button).click()

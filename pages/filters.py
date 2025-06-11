from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Filters(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sort_dropdown = (By.ID, "s-result-sort-select")
        self.low_to_high_option = (By.XPATH, "//option[@value='price-asc-rank']")

    def filter_by_brand(self, brand):
        checkbox = (By.XPATH, f"//li[@aria-label='{brand}']//input")
        self.wait_for_element(checkbox).click()

    def sort_by_price_asc(self):
        self.wait_for_element(self.sort_dropdown).click()
        self.wait_for_element(self.low_to_high_option).click()

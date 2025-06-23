from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Results(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.result_titles = (By.CSS_SELECTOR, "h2 a span")
        self.result_prices_whole = (By.CSS_SELECTOR, "span.a-price-whole")
        self.result_prices_fraction = (By.CSS_SELECTOR, "span.a-price-fraction")

    def get_first_n_titles(self, n):
        elements = self.driver.find_elements(*self.result_titles)
        return [e.text for e in elements[:n]]

    def get_first_n_prices(self, n):
        whole = self.driver.find_elements(*self.result_prices_whole)
        fraction = self.driver.find_elements(*self.result_prices_fraction)
        prices = []
        for w, f in zip(whole[:n], fraction[:n]):
            try:
                price = float(f"{w.text}.{f.text}")
                prices.append(price)
            except:
                continue
        return prices

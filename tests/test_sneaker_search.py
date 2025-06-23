import pytest
import configparser
from selenium import webdriver

from pages.search import Search
from pages.filters import Filters
from pages.results import Results

config = configparser.ConfigParser()
config.read('config.conf')
brand = config.get("Preferences", "BRAND").upper()
base_url = config.get("Preferences", "BASE_PAGE")
product = config.get("Preferences", "PRODUCT")

def test_search_puma_sorted(driver):
    driver.get(base_url)

    search = Search(driver)
    search.search(product)

    filters = Filters(driver)
    filters.filter_by_brand(brand)
    filters.sort_by_price_asc()

    results = Results(driver)
    prices = results.get_first_n_prices(10)
    titles = results.get_first_n_titles(10)

    assert prices == sorted(prices), f"Prices are not in correct order: {prices}"

    for i, title in enumerate(titles):
        assert brand in title.upper(), f"This item #{i+1} is not {brand}: {title}"

import pytest
import json
from selenium import webdriver
from pages.header import Header
from pages.amazon_music import AmazonMusic

with open("config.json", "r") as file:
    config = json.load(file)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_amazon_music(driver):
    driver.get(config.get("BASE_URL"))

    header = Header(driver)
    header.click_music()

    amazon_music = AmazonMusic(driver)

    print("Page title:", driver.title)
    print("URL:", driver.current_url)

    current_path = driver.current_url

    assert config.get("MUSIC_URL") in current_path, f"Expected {config.get('MUSIC_URL')}, but was on {driver.current_url}"
    assert amazon_music.is_at_music_page(), "Amazon Music page is not visible/displayed"

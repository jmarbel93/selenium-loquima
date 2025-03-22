import pytest
from selenium import webdriver
from pages.header import Header
from pages.amazon_music import AmazonMusic
from config import Config

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_amazon_music(driver):
    driver.get(Config.BASE_URL)

    header = Header(driver)
    header.click_music()

    amazon_music = AmazonMusic(driver)

    print("Page title:", driver.title)
    print("URL:", driver.current_url)

    assert Config.MUSIC_URL in driver.current_url, f"Expected {Config.MUSIC_URL}, but was on {driver.current_url}"
    assert amazon_music.is_at_music_page(), "Amazon Music logo not found"






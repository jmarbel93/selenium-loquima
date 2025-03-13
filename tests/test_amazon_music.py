import pytest
from selenium import webdriver
from pages.header import Header
from pages.amazon_music import AmazonMusic

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_amazon_music(driver):
    driver.get("https://www.amazon.es/")
    
    header = Header(driver)
    header.click_music()

    amazon_music = AmazonMusic(driver)
    
    print("Page title:", driver.title)
    print("URL:", driver.current_url)

    assert "amazon.es/music/player" in driver.current_url, f"Expected to be on the Amazon Music page, but was on {driver.current_url}"



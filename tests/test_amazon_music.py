import pytest
import configparser
from pages.base_page import BasePage
from selenium import webdriver
from pages.header import Header
from pages.amazon_music import AmazonMusic

config = configparser.ConfigParser()
config.read('config.conf')

def test_amazon_music(driver):
    driver.get(config.get("Preferences", "BASE_PAGE"))

    header = Header(driver)
    header.click_music()

    amazon_music = AmazonMusic(driver)

    print("Page title:", driver.title)
    print("URL:", driver.current_url)

    current_path = driver.current_url

    assert config.get("Preferences", "MUSIC_URL") in current_path, f"Expected {config.get('Preferences', 'MUSIC_URL')}, but was on {driver.current_url}"
    assert amazon_music.is_visible(), "Amazon Music page is not visible/displayed"

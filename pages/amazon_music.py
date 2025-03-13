from selenium.webdriver.common.by import By

class AmazonMusic:
    def __init__(self, driver):
        self.driver = driver

    def is_at_music_page(self):
        return "amazon.es/music/player" in self.driver.current_url



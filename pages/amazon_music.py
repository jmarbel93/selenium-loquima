from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AmazonMusic(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.music_logo = (By.ID, "navbarMusicLogo")
    
    def is_visible(self):
        return super().is_visible(self.music_logo)

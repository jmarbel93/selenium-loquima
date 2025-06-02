from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.music_link = (By.ID, "music")
    
    def click_music(self):
        self.click(self.music_link)

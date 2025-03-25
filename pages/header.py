from selenium.webdriver.common.by import By

class Header:
    def __init__(self, driver):
        self.driver = driver
        self.music_link = (By.ID, "music")

    def click_music(self):
        self.driver.find_element(*self.music_link).click()

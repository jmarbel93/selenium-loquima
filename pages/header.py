from selenium.webdriver.common.by import By

class Header:
    def __init__(self, driver):
        self.driver = driver
        self.music_link = (By.LINK_TEXT, "Música") 

    def click_music(self):
        music_button = self.driver.find_element(*self.music_link)
        music_button.click()

from selenium.webdriver.common.by import By

class AmazonMusic:
    def __init__(self, driver):
        self.driver = driver
        self.music_logo = (By.ID, "navbarMusicLogo")

    def is_at_music_page(self):
        return len(self.driver.find_elements(*self.music_logo)) > 0






import time, math
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class YoutubePlayer:
    driver: Chrome = None
    
    def __init__(self, driver: Chrome):
        self.driver = driver
        
    def enlarge_screen(self):
        full_screen_button = self.driver.find_element(By.XPATH, '//button[contains(@class, "ytp-fullscreen-button")]')
        full_screen_button.click()
        
    def play(self):
        play_button = self.driver.find_element(By.CLASS_NAME, 'ytp-large-play-button')
        play_button.click()
        
    
    def get_current_time(self) -> int:
        current_time = self.driver.execute_script("return document.querySelector('video').currentTime")
        return math.floor(current_time)

    
    def get_total(self) -> int:
        duration_str = self.driver.find_element(
        By.CLASS_NAME, 'ytp-time-duration').get_attribute('innerHTML').split(':')
        return int(duration_str[0]) * 60 + int(duration_str[1])
    
    def get_duration(self) -> int:
        return self.get_total() - self.get_current_time()
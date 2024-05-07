import sys
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import from utils.py
from utils.utils import get_last_episode, write_last_episode, open_browser,get_driver

driver = get_driver()


def get_jujutsu_url(episode_number):
    return f'https://silkysub.com/watch/jujutsu-kaisen/season/1/episode/{str(episode_number)}'

def start_player(self):
    playBtn = driver.find_element(By.XPATH, '//button[contains(@class, "bg-[#850d0d]")]')
    playBtn.click()
    
    # switch to iframe 1
    frame = driver.find_element(By.XPATH, '//iframe[contains(@class, "w-full")]')
    print(frame)
    driver.switch_to.frame(frame)
    time.sleep(3)
    print("switched to new iframe")
    # click start
    startBtn = driver.find_element(By.XPATH, '//div[@data-tooltip="הפעלה"]')
    print(f'startBtn: {startBtn}')
    startBtn.click()
    time.sleep(2)
    iframe2 = driver.find_element(By.ID, 'drive-viewer-video-player-object-0')
    driver.switch_to.frame(iframe2)
    self.set_youtube_player()
    
    time.sleep(1)
    full_screen_button = driver.find_element(By.XPATH, '//button[contains(@class, "ytp-fullscreen-button")]')
    full_screen_button.click()
    time.sleep(2)
    final_play_button = driver.find_element(By.CLASS_NAME, 'ytp-large-play-button')
    final_play_button.click()
    
# def start_video_interval():
    


def play(episode_number):
    print(f'Start episode {episode_number}')
    write_last_episode(episode_number)
    url = get_jujutsu_url(episode_number)
    open_browser(driver,url)
    start_player()
    # start_video_interval()
    # time.sleep(4)
    # go_to_next_episode(episode_number)

def init(param):
    if param == "last":
        print(get_last_episode())
    if param == "play":
        play(int(get_last_episode()) + 1)
    else:
        play(param)

init(sys.argv[1])

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time
import os
from pprint import pprint 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.utils import get_last_episode, write_last_episode, open_browser, get_driver


driver = get_driver()

video_start_time = 60 * 4
video_time_from_end = 40  # in seconds


def get_one_piece_url(episode_number):
    return f'https://animeisrael.website/watch/fulllink/op/fulllinkop-{str(episode_number)}.php'


control_video_script = f"""
const video = document.getElementsByTagName('video').item(0);
video.currentTime = {video_start_time};
"""
scroll_to_video_script = f"""
const iframe = document.getElementsByTagName('iframe').item(0);
iframe.scrollIntoView(true)
"""


def start_player():
    iframe1 = driver.find_element(By.CLASS_NAME, "embed-responsive-item")
    driver.execute_script(scroll_to_video_script)
    time.sleep(2)
    driver.switch_to.frame(iframe1)
    showPlayer = driver.find_element(By.TAG_NAME, 'img')
    ActionChains(driver).move_to_element(
        showPlayer).click(showPlayer).perform()
    time.sleep(1)
    iframe2 = driver.find_element(By.ID, 'drive-viewer-video-player-object-0')
    driver.switch_to.frame(iframe2)
    time.sleep(1)
    driver.execute_script(control_video_script)
    time.sleep(1)
    full_screen_button = driver.find_element(
        By.CLASS_NAME, 'ytp-fullscreen-button')
    ActionChains(driver).move_to_element(
        full_screen_button).click(full_screen_button).perform()
    time.sleep(2)
    play_button = driver.find_element(By.CLASS_NAME, 'ytp-large-play-button')
    ActionChains(driver).move_to_element(
        play_button).click(play_button).perform()


def check_video_duration():
    current_time_str = driver.find_element(
        By.CLASS_NAME, 'ytp-time-current').get_attribute('innerHTML').split(':')
    current_time = int(current_time_str[0]) * 60 + int(current_time_str[1])
    duration_str = driver.find_element(
        By.CLASS_NAME, 'ytp-time-duration').get_attribute('innerHTML').split(':')
    duration = int(duration_str[0]) * 60 + int(duration_str[1])
    return current_time + video_time_from_end > duration


def start_video_interval():
    is_video_over = check_video_duration()
    while is_video_over == False:
        time.sleep(1)
        is_video_over = check_video_duration()


def go_to_next_episode(episode_number):
    play(int(episode_number) + 1)


def play(episode_number):
    print('Start episode ' + str(episode_number))
    write_last_episode(episode_number)
    url = get_one_piece_url(episode_number)
    open_browser(driver,url)
    start_player()
    start_video_interval()
    time.sleep(4)
    go_to_next_episode(episode_number)

def init(param):
    if param == "last":
        print(get_last_episode())
    if param == "play":
        play(int(get_last_episode()) + 1)
    else:
        play(param)

init(sys.argv[1])

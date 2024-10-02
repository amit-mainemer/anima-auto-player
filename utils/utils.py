import time
import json
import os
from selenium import webdriver

FILE_NAME = "data.json"
LAST_KEY = "last"

CONTROL_VIDEO_SCRIPT= f"""
    const video = document.getElementsByTagName('video').item(0);
    video.currentTime = {str(60 * 4)};
    """

def open_browser(driver, url):
    driver.get(url)
    time.sleep(1)
    driver.maximize_window()
    time.sleep(2)

def write_last_episode(key: str, last_episode):
    if os.path.isfile(FILE_NAME):
        f = open(FILE_NAME, "r")
        raw = f.read()
        f.close()
        data = json.loads(raw)
        if key in data:
            data[key][LAST_KEY] = last_episode
            f = open(FILE_NAME, "w")
            f.write(json.dumps(data))
        else:
            data[key] = {}
            data[key][LAST_KEY] = last_episode
            f = open(FILE_NAME, "w")
            f.write(json.dumps(data))
    else:
        f = open(FILE_NAME, "w")
        data = {}
        data[key] = {}
        data[key][LAST_KEY] = last_episode
        print(f"data: {data}")
        f = open(FILE_NAME, "w")
        f.write(json.dumps(data))
        
def get_last_episode(key: str)->int:
    if os.path.isfile(FILE_NAME):
        f = open(FILE_NAME, "r")
        raw = f.read()
        f.close()
        data = json.loads(raw)
        if key in data:
            return data[key][LAST_KEY]
        else:
            print(f"data: No key in json {key}")
            return 1
    else:
        return 1


def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    return webdriver.Chrome(options=chrome_options)


    
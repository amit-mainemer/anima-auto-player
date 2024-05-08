import sys, os, time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.YoutubePlayer import YoutubePlayer
from utils.utils import get_last_episode, write_last_episode, open_browser
from utils.AnimaPlayer import AnimaPlayer


class JujutsuPlayer(AnimaPlayer):
    KEY="ju"
    EPISODE_END_SKIP=100
    def __init__(self, driver: Chrome):
        super().__init__(driver)
    
    def play(self, episode_number):
        self.print(f'Start episode {episode_number}')
        self.save_last_episode(episode_number)
        url = self.get_jujutsu_url(episode_number)
        open_browser(self.driver,url)
        self.start()
        self.start_video_interval()
        self.go_to_next_episode(episode_number)
    
    def start(self):
        playBtn = self.driver.find_element(By.XPATH, '//button[contains(@class, "bg-[#850d0d]")]')
        playBtn.click()
        time.sleep(1)
        frame =  self.driver.find_element(By.XPATH, '//iframe[contains(@class, "w-full")]')
        self.driver.switch_to.frame(frame)
        time.sleep(3)
        # click start
        startBtn =  self.driver.find_element(By.XPATH, '//div[@data-tooltip="הפעלה"]')
        startBtn.click()
        time.sleep(2)
        iframe2 =  self.driver.find_element(By.ID, 'drive-viewer-video-player-object-0')
        self.driver.switch_to.frame(iframe2)
        time.sleep(1)
        self.set_youtube_player()
        self.youtubePlayer.enlarge_screen()
        self.youtubePlayer.play()
        time.sleep(2)
        
    def check_video_duration(self) -> bool:
        duration = self.youtubePlayer.get_duration()
        return self.EPISODE_END_SKIP > duration
        
    def start_video_interval(self):
        is_video_over = self.check_video_duration()
        while is_video_over == False:
            time.sleep(1)
            is_video_over = self.check_video_duration()
        
    def go_to_next_episode(self, episode_number):
        self.play(int(episode_number) + 1)
    
    @staticmethod
    def get_jujutsu_url(episode_number: int) -> str:
        return f'https://silkysub.com/watch/jujutsu-kaisen/season/1/episode/{str(episode_number)}'
    
    def save_last_episode(self, episode: int):
        write_last_episode(self.KEY, episode)
    
    def get_last_episode(self)->int:
        return get_last_episode(self.KEY)
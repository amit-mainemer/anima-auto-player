import sys, os, time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.YoutubePlayer import YoutubePlayer
from utils.utils import get_last_episode, write_last_episode, open_browser
from utils.AnimaPlayer import AnimaPlayer
from utils.utils import CONTROL_VIDEO_SCRIPT


class BlackCloverPlayer(AnimaPlayer):
    KEY="bc"
    EPISODE_END_SKIP=100
    
    def __init__(self, driver: Chrome):
        super().__init__(driver)
    
    def play(self, episode_number):
        self.print(f'Start episode {episode_number}')
        self.save_last_episode(episode_number)
        url = self.get_black_clover_url()
        open_browser(self.driver,url)
        self.start(episode_number)
        self.start_video_interval()
        self.go_to_next_episode(episode_number)
    
    def start(self, episode_number: int):
        time.sleep(4)
        frame =  self.driver.find_element(By.XPATH, '//iframe[contains(@class, "wuksD5")]')
        self.driver.switch_to.frame(frame)
        time.sleep(3)
        
        # JavaScript to find and click the button by its text content
        script = f"""
        const elements = document.querySelectorAll('.episode-button');
        const btns = [...elements]
        const button = btns.find((btn) => btn.innerText.includes('{str(episode_number)}'))
        console.log("button =>", button)
        if (button) 
            button.click();
        """
        
        # Execute the JavaScript in the browser to click the button
        self.driver.execute_script(script)
        time.sleep(2)
        frame2 =  self.driver.find_element(By.ID, 'videoFrame')
        self.driver.switch_to.frame(frame2)
        time.sleep(2)
        # click start
        startBtn = self.driver.find_element(By.XPATH, "//div[@role='button' and @data-tooltip='הפעלה']")
        startBtn.click()
        time.sleep(3)
        frame3 =  self.driver.find_element(By.ID, 'drive-viewer-video-player-object-0')
        self.driver.switch_to.frame(frame3)
        time.sleep(1)
        self.set_youtube_player()
        self.youtubePlayer.enlarge_screen()
        self.driver.execute_script(CONTROL_VIDEO_SCRIPT)
        time.sleep(1)
        self.youtubePlayer.play()
        
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
    def get_black_clover_url() -> str:
        return f'https://www.animeil-tv.com/bc'
    
    def save_last_episode(self, episode: int):
        write_last_episode(self.KEY, episode)
    
    def get_last_episode(self)->int:
        return get_last_episode(self.KEY)
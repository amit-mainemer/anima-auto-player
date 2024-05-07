
import sys, os, time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.YoutubePlayer import  YoutubePlayer
from utils.utils import get_last_episode, write_last_episode, open_browser
from utils.AnimaPlayer import AnimaPlayer

class OnePiecePlayer(AnimaPlayer):
    KEY="op"
    CONTROL_VIDEO_SCRIPT= f"""
    const video = document.getElementsByTagName('video').item(0);
    video.currentTime = {str(60 * 4)};
    """
    SCROLL_TO_VIDEO_SCRIPT = f"""
    const iframe = document.getElementsByTagName('iframe').item(0);
    iframe.scrollIntoView(true)
    """
    EPISODE_END_SKIP=60
    youPlayer: YoutubePlayer = None
    
    def __init__(self, driver: Chrome):
        super().__init__(driver)
        
    def play(self, episode_number):
        print(f'Start episode {str(episode_number)}')
        self.save_last_episode(episode_number)
        url = self.get_url(episode_number)
        open_browser(self.driver,url)
        self.start()
        self.start_video_interval()
        time.sleep(1)
        self.go_to_next_episode(episode_number)
        
    def go_to_next_episode(self, episode_number):
        self.play(episode_number + 1)
    
    @staticmethod
    def get_url(episode_number: int):
            return f'https://animeisrael.website/watch/fulllink/op/fulllinkop-{str(episode_number)}.php'
    
    def start(self):
        iframe1 = self.driver.find_element(By.CLASS_NAME, "embed-responsive-item")
        self.driver.execute_script(self.SCROLL_TO_VIDEO_SCRIPT)
        time.sleep(2)
        self.driver.switch_to.frame(iframe1)
        showPlayer = self.driver.find_element(By.TAG_NAME, 'img')
        ActionChains(self.driver).move_to_element(
            showPlayer).click(showPlayer).perform()
        time.sleep(1)
        iframe2 = self.driver.find_element(By.ID, 'drive-viewer-video-player-object-0')
        self.driver.switch_to.frame(iframe2)
        time.sleep(1)
        self.driver.execute_script(self.CONTROL_VIDEO_SCRIPT)
        time.sleep(1)
        self.set_youtube_player()
        self.youtubePlayer.enlarge_screen()
        self.youtubePlayer.play()
        
    def check_video_duration(self) -> bool:
        duration = self.youtubePlayer.get_duration()
        return self.EPISODE_END_SKIP > duration


    def start_video_interval(self):
        is_video_over = self.check_video_duration()
        while is_video_over == False:
            time.sleep(1)
            is_video_over = self.check_video_duration()

    def save_last_episode(self, episode: int):
        write_last_episode(self.KEY, episode)
    
    def get_last_episode(self)->int:
        return get_last_episode(self.KEY)
    
from selenium.webdriver import Chrome
from abc import abstractmethod
from utils.YoutubePlayer import YoutubePlayer

class AnimaPlayer:
    driver: Chrome = None
    youtubePlayer: YoutubePlayer = None
    
    def __init__(self, driver: Chrome):
        self.driver = driver
    
    @abstractmethod
    def play(self, episode_number: int):
        pass
    
    @abstractmethod
    def get_last_episode(self)->int:
        pass
    
    def set_youtube_player(self):
        self.youtubePlayer = YoutubePlayer(self.driver)
        
    def print(self, text: str):
        print(f"{self.__class__.__name__}: {text}")

import sys
from typing import Dict
from OnePiece.OnePiecePlayer import OnePiecePlayer
from Jujutsu.JujutsuPlayer import JujutsuPlayer
from BlackClover.BlackCloverPlayer import BlackCloverPlayer
from utils.AnimaPlayer import AnimaPlayer
from utils.utils import get_driver

LIST="\nAnima List\nop = One Piece\nju = Jujutsu Kaisen\nbc = Black Clover"
HELP=f"""
In order to play the anima, write your required show and then one of the following commands in this pattern:
anima [anima show] [command|number] \n
{LIST}

Command:
again = paly the latest episode that was played
play = play the latest episode that was played + 1
last = get the latest episode that was played
[number] = play the stated episode number
"""

animaPlayerMap: Dict[str, AnimaPlayer] = {
    OnePiecePlayer.KEY: OnePiecePlayer,
    JujutsuPlayer.KEY: JujutsuPlayer,
    BlackCloverPlayer.KEY: BlackCloverPlayer
}


def init(params):
    if(params[1] == "list"):
        print(LIST)
        return
  
    if(params[1] == "help"):
        print(HELP)
        return

    if params[1] in animaPlayerMap:
        driver = get_driver()
        animaPlayer: AnimaPlayer = animaPlayerMap[params[1]](driver)
        last_episode = animaPlayer.get_last_episode()
        if(len(params) < 3): 
            print("Please write a command or episode number. (you can view [anima help])")
            return
        if(params[2] == "last"):
            print(last_episode)
            return
        if(params[2] == "play"):
            animaPlayer.play(int(last_episode) + 1)
        if(params[2] == "again"):
            animaPlayer.play(last_episode)
        else:
            animaPlayer.play(params[2])
    else:
        print("Invalid argument. you can type [anima help] to view all possible options")
            


init(sys.argv)
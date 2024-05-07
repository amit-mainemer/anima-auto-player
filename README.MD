# Anima Player

This project is for viewing anima in an automated way (Netflix style)
 
## Setup
1. You will need to install python on your computer you can find it here:  
[Download Python](https://www.python.org/downloads/)
 
2. if youre on windows it is recommended to install [Git bash](https://git-scm.com/downloads) 

3. In order to play you will need to add to your .bash_profile file the aliases for the file anima player path and the python exec command. Example:

```bash
alias op="cd {path_to_project}/onePiecePyPlayer/OnePiece && python main.py $1"
alias ju="cd {path_to_project}/onePiecePyPlayer/Jujutsu && python main.py $1"
# and so on for the others
```
4. After you finished this you can open your terminal and run one of the following:
```bash
op play #this will run the latest episode you played
op {episode_number} #this will run the episode you stated
```

## Enjoy!
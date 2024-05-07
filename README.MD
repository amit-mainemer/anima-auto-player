# Anima Auto Player

This project is for viewing anima in an automated way (Netflix style)
 
## Setup
1. You will need to install python on your computer you can find it here:  
[Download Python](https://www.python.org/downloads/)
 
2. if your using windows it is recommended to install [Git bash](https://git-scm.com/downloads) 

3. In order to execute the script you will need to add to your .bash_profile file the alias for the file anima player path and the python exec command. Like this:

```bash
alias anima="cd /c/Projects/onePiecePyPlayer && python anima.py $1 $2"
```
4. After you finished this you can open your terminal and run one of the following:
```bash
anima list #list of all the anima shows and their shortcuts
anima help #A guide how to use the tool
anima {anima_show_shortcut} play #this will run the latest episode you played
anima {anima_show_shortcut} {episode_number} #this will run the episode you stated
```

## Enjoy!
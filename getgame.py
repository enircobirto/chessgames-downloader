from msvcrt import getch
import requests
import re

def getgame(game):
    gid = game.split("gid=")[1]
    url = f'https://www.chessgames.com/nodejs/game/viewGamePGN?text=1&gid={gid}'
    headers = {
        'User-Agent':'Mozilla/5.0',
    }
    r = requests.get(url, headers=headers) 

    lines=r.text.split('\n')
    nonemptylines=[line for line in lines if line.strip()!='']
    result=""
    for line in nonemptylines:
        result+=line+'\n'
    return r.text+'\n'
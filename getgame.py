import requests
import re

def getgame(game):
    result = open("result.pgn","a",encoding='utf-8')
    gid = game.split("gid=")[1]
    url = f'https://www.chessgames.com/nodejs/game/viewGamePGN?text=1&gid={gid}'
    headers = {
        'User-Agent':'Mozilla/5.0',
    }
    r = requests.get(url, headers=headers) 
    result.write(r.text+'\n')

    return r.text
import requests

def getgame(game):
    gid = game.split("gid=")[1]
    url = f'https://www.chessgames.com/nodejs/game/viewGamePGN?text=1&gid={gid}'
    headers = {
        'User-Agent':'Mozilla/5.0'
    }
    r = requests.get(url, headers=headers) 
    return r.text
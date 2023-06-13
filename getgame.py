import requests

def getgame(game):
    result = open("result.pgn","a")
    gid = game.split("gid=")[1]
    url = f'https://www.chessgames.com/nodejs/game/viewGamePGN?text=1&gid={gid}'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept-Encoding': 'identity'
    }
    r = requests.get(url, headers=headers) 
    result.write(r.text)
    print(r.text)
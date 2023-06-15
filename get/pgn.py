from difflib import SequenceMatcher
import requests
import re

def pgn(info):
    game=info[0]
    options=info[1]
    gid = game.split("gid=")[1]
    player = game.split("player=")[1]
    url = f'https://www.chessgames.com/nodejs/game/viewGamePGN?text=1&gid={gid}'
    headers = {
        'User-Agent':'Mozilla/5.0',
    }
    r = requests.get(url, headers=headers) 

    result=r.text

    if options['white_only']:
        try:
            white = re.findall(r'White "(.*?)"',result)[0]
        except:
            return ''
        if similar(player,white) >= 0.7:
            return result+'\n'
        else:
            return ''
    if options['black_only']:
        try:
            black = re.findall(r'Black "(.*?)"',result)[0]
        except:
            return ''
        if similar(player,black) >= 0.7:
            return result+'\n'
        else:
            return ''

    return r.text+'\n'

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

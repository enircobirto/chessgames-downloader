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

    lines=r.text.split('\n')
    nonemptylines=[line for line in lines if line.strip()!='']
    result=""
    for line in nonemptylines:
        result+=line+'\n'

    if options['white_only']:
        try:
            white = re.findall(r'White "(.*?)"',result)[0]
        except:
            return ''
        if similar(player,white) >= 0.7:
            print(f"white: {white}, exporting.")
            return result+'\n'
        else:
            print(f"white: {white}, NOT exporting.")
            return ''
    if options['black_only']:
        try:
            black = re.findall(r'Black "(.*?)"',result)[0]
        except:
            return ''
        if similar(player,black) >= 0.7:
            print(f"black: {black}, exporting.")
            return result+'\n'
        else:
            print(f"black: {black}, NOT exporting.")
            return ''

    return result+'\n'

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

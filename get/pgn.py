import requests
import re

def pgn(info):
    game=info[0]
    options=info[1]
    players=info[2]
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

    if options['white_only']:
        white = re.findall(r'White "(.*?)"',result)[0]
        if white in players:
            print(f"white: {white}, exporting.")
            return result+'\n'
        else:
            print(f"white: {white}, NOT exporting.")
            return ''
    if options['black_only']:
        black = re.findall(r'Black "(.*?)"',result)[0]
        if black in players:
            print(f"black: {black}, exporting.")
            return result+'\n'
        else:
            print(f"black: {black}, NOT exporting.")
            return ''

    return result+'\n'

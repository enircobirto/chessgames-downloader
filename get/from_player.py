from alive_progress import alive_bar
import requests
import json
import re

def from_player(player):
    try:
        url=f"https://www.chessgames.com/perl/ezsearch.pl?search={player}"
        headers = {
            'User-Agent':'Mozilla/5.0',
        }
        page = requests.get(url, headers=headers) 
        pid = get_pid(page.text)
        page=requests.get(f"https://www.chessgames.com/perl/chess.pl?page=1&pid={pid}",headers=headers)
        pageCount = get_page_count(page.text)

        info = dict({"player":player.strip(),"pid":pid,"max":pageCount})
        return info

        #return (f"\n-> {player}: {pageCount} pages")
    except:
        info = dict({"player":player.strip(),"pid":'ERROR',"max":'ERROR'})
        return info

def get_pid(page):
    return re.findall(r'Player profile: <B><a href="/perl/chessplayer\?pid=(.*)">',page)[0]
def get_page_count(page):
    return int(re.findall(r'page 1 of (.*?);',page)[0])

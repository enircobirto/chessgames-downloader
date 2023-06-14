from alive_progress import alive_bar
import requests
import json
import re

def getfromplayer(player):
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
        pass
        return (f"-> Error getting info from {player}")

def getfrompage(page):
    headers = {
        'User-Agent':'Mozilla/5.0',
    }
    content=requests.get(f"https://www.chessgames.com/perl/chess.pl?page={page['page']}&pid={page['pid']}",headers=headers)
    get_game_list(content.text)
    return (f"> wrote page {page['page']} from {page['player']}")
        
            
def get_pid(page):
    return re.findall(r'Player profile: <B><a href="/perl/chessplayer\?pid=(.*)">',page)[0]
def get_page_count(page):
    return int(re.findall(r'page 1 of (.*?);',page)[0])
def get_game_list(page):
    links = re.findall(r'<a href="/perl/chessgame\?gid=(.*?)">',page)
    for link in links:
        gamelist = open("gamelist.txt","a")
        gamelist.write(f"https://www.chessgames.com/perl/chessgame?gid={str(link)}\n")
        gamelist.close()

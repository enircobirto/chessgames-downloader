import re
import requests


def getfrompage(page):
    headers = {
        'User-Agent':'Mozilla/5.0',
    }
    content=requests.get(f"https://www.chessgames.com/perl/chess.pl?page={page['page']}&pid={page['pid']}",headers=headers)
    get_game_list(content.text)
    return (f"> wrote page {page['page']} from {page['player']}")

def get_game_list(page):
    links = re.findall(r'<a href="/perl/chessgame\?gid=(.*?)">',page)
    for link in links:
        gamelist = open("gamelist","a+")
        gamelist.write(f"https://www.chessgames.com/perl/chessgame?gid={str(link)}\n")
        gamelist.close()
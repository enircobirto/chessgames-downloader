import re
import requests

def from_page(page):
    headers = {
        'User-Agent':'Mozilla/5.0',
    }
    content=requests.get(f"https://www.chessgames.com/perl/chess.pl?page={page['page']}&pid={page['pid']}",headers=headers)
    return (get_game_list(content.text,page['pid']))

def get_game_list(page,pid):
    links = re.findall(r'<a href="/perl/chessgame\?gid=(.*?)">',page)
    gamelist=[]
    for link in links:
        gamelist.append(f"https://www.chessgames.com/perl/chessgame?gid={str(link)}?player={get_player_name(page,pid).replace(' ','_')}\n")
    return gamelist

def get_player_name(page,pid):
    return re.findall(f'{pid}">(.*?)\n',page)[0]

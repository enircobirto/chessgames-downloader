import re
from alive_progress import alive_bar
from multiprocessing import Pool
from itertools import repeat

import requests

from get.from_page import from_page

def get_page_list(info,spaces,n,options):
    player=info['player']
    pages=[]
    
    if options['white_only'] or options['black_only']:
        with alive_bar(int(info['max']),title=f' > Extracting Pages from {player}',bar='classic',spinner='classic') as bar:
            with Pool(n) as pool:
                for result in pool.imap_unordered(get_page_links,zip(range (1,int(info['max'])+1),repeat(info['pid']))):
                    bar()
                    pages.append(result)

        for page in pages:
            get_game_links(page,options,info['player'],info['pid'],n)
    else:
        pagelist=[]
        for num in range(1,int(info['max'])):
            pagelist.append(dict({
                'player':info['player'],
                'pid':info['pid'],
                'page':num
            }))
        with alive_bar(len(pagelist),title=f' > Extracting pages   {spaces}',bar='filling',spinner='classic') as bar:
            with Pool(n) as pool:
                for result in pool.imap_unordered(from_page,pagelist):
                    bar()
    
def get_page_links(zipped):
    i=zipped[0]
    pid=zipped[1]
    
    content=requests.get(
        url=f"https://www.chessgames.com/perl/chess.pl?page={i}&pid={pid}",
        headers={'User-Agent':'Mozilla/5.0'}
        ).text
    return content

def get_game_links(page,options,player,pid,n):
    gids = re.findall(r'<a href="/perl/chessgame\?gid=(.*?)">',page)
    games = re.findall(r'>.nbsp;page .*? of .*?; games (.*?) of .*?nbsp;<',page)[0]
    
    gamelinks=[]
    with alive_bar(len(gids),title=f' > Games {games} from {player}',bar='classic',spinner='classic') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(get_games,zip(gids,repeat(pid),repeat(options))):
                gamelinks.append(result)
                bar()
    
    gamelist=open("gamelist","a",encoding='utf-8')
    for game in gamelinks:
        gamelist.write(game)
    gamelist.close()

def get_games(zipped):
    gid=zipped[0]
    pid=zipped[1]
    options=zipped[2]
    url = f"https://www.chessgames.com/perl/chessgame?gid={str(gid)}\n"
    if validate(url,pid,options):
        return url
    else:
        return ''


def validate(link,pid,options):
    if options['white_only']:
        headers = {
            'User-Agent':'Mozilla/5.0',
        }
        content=requests.get(link,headers=headers).text
        white = re.findall(r'pid=(.*?)">.*</a></b>',content)[0]
        if white == pid:
            return True
        else:
            return False

    elif options['black_only']:
        headers = {
            'User-Agent':'Mozilla/5.0',
        }
        content=requests.get(link,headers=headers).text

        black = re.findall(r'pid=(.*?)">.*</a></b>')[1]

        if black == pid:
            return True
        else:
            return False
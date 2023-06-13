from alive_progress import alive_bar
import requests
import re

def getfromplayer(player):
    url=f"https://www.chessgames.com/perl/ezsearch.pl?search={player}"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept-Encoding': 'identity'
    }
    page = requests.get(url, headers=headers) 
    print(f"\n\n> {player}")
    with alive_bar(theme='classic',length='5') as bar:
        bar.title(f'-> Fetching')
        pid = get_pid(page.text)
        print(pid)

        page=requests.get(f"https://www.chessgames.com/perl/chess.pl?page=1&pid={pid}",headers=headers)
        i=1
        pageCount = get_page_count(page.text)
    with alive_bar(pageCount,enrich_print=True,bar='filling',spinner='classic') as bar:
        bar.title(f'-> Getting from pages')
        while i<=pageCount:
            page=requests.get(f"https://www.chessgames.com/perl/chess.pl?page={i}&pid={pid}",headers=headers)
            get_game_list(page.text)
            i+=1
            bar(1)
            
def get_pid(page):
    return re.findall(r'Player profile: <B><a href="/perl/chessplayer\?pid=(.*)">',page)
def get_page_count(page):
    return int(re.findall(r'page 1 of (.*?);',page)[0])
def get_game_list(page):
    links = re.findall(r'<a href="/perl/chessgame\?gid=(.*?)">',page)
    for link in links:
        gamelist = open("gamelist.txt","a")
        gamelist.write(f"https://www.chessgames.com/perl/chessgame?gid={str(link)}\n")
        gamelist.close()
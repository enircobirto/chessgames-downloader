from src.GameList import GameList
from src.Home import Home
from src.Search import Search
from alive_progress import alive_bar

def getfromplayer(driver,player):
    driver.get("https://www.chessgames.com/")
    home = Home(driver)
    home.type_player(player)
    # home.search()
    print(f"\n\n> {player}")
    with alive_bar(theme='classic',length='5') as bar:
        bar.title(f'-> Fetching')
        search = Search(driver)
        pid = search.get_pid().split("pid=")[1]

        driver.get(f"https://www.chessgames.com/perl/chessplayer?pid={pid}")

        games="\n"
    
        driver.get(f"https://www.chessgames.com/perl/chess.pl?page=1&pid={pid}")
        gameList = GameList(driver)
        i=1
        pageCount = gameList.get_page_count()
        
    with alive_bar(pageCount,enrich_print=True,bar='filling',spinner='classic') as bar:
        bar.title(f'-> Getting from pages')
        while i<=pageCount:
            driver.get(f"https://www.chessgames.com/perl/chess.pl?page={i}&pid={pid}")
            gameList = GameList(driver)
            gameList.get_game_list()
            i+=1
            bar(1)
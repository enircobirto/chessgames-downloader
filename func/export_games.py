
from multiprocessing import Pool
from alive_progress import alive_bar

from get.pgn import pgn

def export_games(path,n):
    try:
        gamelist = open("gamelist", "r", encoding='utf-8').readlines()
    except:
        gamelist = open("gamelist", "w", encoding='utf-8')
        gamelist.close()
        gamelist = open("gamelist", "r", encoding='utf-8').readlines()

    with alive_bar(len(gamelist),title=f' > Exporting games to {path}',bar='filling',spinner='classic') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(pgn,gamelist):
                bar()
                output = open(path,"a+",encoding='utf-8')
                output.write(result)
                output.close()
    gamelist = open("gamelist", "w", encoding='utf-8')
    gamelist.close()

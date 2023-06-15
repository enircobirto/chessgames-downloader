from multiprocessing import Pool
from alive_progress import alive_bar
from itertools import repeat

from get.pgn import pgn

def export_games(path,n,options,spaces):
    try:
        gamelist = open("gamelist", "r", encoding='utf-8').readlines()
    except:
        gamelist = open("gamelist", "w", encoding='utf-8')
        gamelist.close()
        gamelist = open("gamelist", "r", encoding='utf-8').readlines()

    resultlist=[]
    with alive_bar(len(gamelist),title=f' > Writing games      {spaces}',bar='filling',spinner='classic') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(pgn,zip(gamelist,repeat(options))):
                if result!= '':
                    bar()
                    resultlist.append(result)
                else:
                    bar(skipped=True)
                    
    with alive_bar(len(resultlist),title=f' > Exporting games to {path}',bar='filling',spinner='classic') as bar:
        output = open(path,"a+",encoding='utf-8')
        for result in resultlist:
            output.write(result)
            bar()
        output.close()
        
    gamelist = open("gamelist", "w", encoding='utf-8')
    gamelist.close()

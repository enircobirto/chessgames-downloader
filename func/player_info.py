from multiprocessing import Pool
from alive_progress import alive_bar

from get.from_player import from_player


def player_info(playerlist,spaces,n):
    info=[]
    with alive_bar(len(playerlist),title=f' > Extracting players {spaces}',bar='filling',spinner='classic') as bar:
       with Pool(n) as pool:
            for result in pool.imap_unordered(from_player,playerlist):
                if result['pid']!='ERROR':
                    info.append(result)
                    bar()
                else:
                    print(f"> Error getting info from {result['player']}")
    return info

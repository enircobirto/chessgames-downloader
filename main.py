from msvcrt import getch
from multiprocessing import Process, Pool
import re

import pandas as pd
from getfromplayer import getfromplayer,getfrompage
from alive_progress import alive_bar
from getgame import getgame
from pprint import pprint

def main():
    playerlist = open("playerlist.txt", "r").readlines()
    
    n = min(len(playerlist),8)
    
    info = []
    
    with alive_bar(len(playerlist),title='Getting info from players',bar='filling',spinner='classic') as bar:
       with Pool(n) as pool:
            for result in pool.imap_unordered(getfromplayer,playerlist):
                print(f"> {result['player']}({result['pid']}): {result['max']} pages")
                info.append(result)
                bar()
    
    pagelist=[]
    for i in info:
        for num in range(1,i['max']):
            pagelist.append(dict({
                'player':i['player'],
                'pid':i['pid'],
                'page':num
            }))
    n = 16 
    with alive_bar(len(pagelist),title='Getting game links from pages',bar='filling',spinner='classic') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(getfrompage,pagelist):
                bar()
    
    gamelist = open("gamelist.txt", "r").readlines()

    section = list(split(gamelist,len(gamelist)//n))
    section.append(gamelist[:-len(gamelist)%n])

    with alive_bar(len(gamelist),title='Exporting games to result.pgn',bar='filling') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(getgame,gamelist):
                bar()
                print(result)

def split(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

if __name__ == "__main__":
    main()

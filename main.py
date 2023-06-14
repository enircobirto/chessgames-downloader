from multiprocessing import Process, Pool
import argparse

from getfromplayer import getfromplayer
from getfrompage import getfrompage
from alive_progress import alive_bar
from getgame import getgame
from pprint import pprint

def main(args):
    try:
        playerlist = open(args.playersfile, "r").readlines()
    except:
        playerlist=[]
    for player in args.players.split(','):
        playerlist.append(f'{player.strip()}\n')

    if(len(playerlist)==0):
        return "<!> Empty player list!"

    n = min(len(playerlist),8)
    
    info = []
    
    with alive_bar(len(playerlist),title='Getting info from players',bar='filling',spinner='classic') as bar:
       with Pool(n) as pool:
            for result in pool.imap_unordered(getfromplayer,playerlist):
                if result['pid']!='ERROR':
                    print(f"> {result['player']}({result['pid']}): {result['max']} pages")
                    info.append(result)
                else:
                    print(f"> Error getting info from {result['player']}")
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
    try:
        gamelist = open("gamelist", "r", encoding='utf-8').readlines()
    except:
        gamelist = open("gamelist", "w", encoding='utf-8')
        gamelist.close()
        gamelist = open("gamelist", "r", encoding='utf-8').readlines()
    section = list(split(gamelist,len(gamelist)//n))
    section.append(gamelist[:-len(gamelist)%n])

    with alive_bar(len(gamelist),title=f'Exporting games to {args.output}',bar='filling',spinner='classic') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(getgame,gamelist):
                bar()
                output = open(args.output,"a+",encoding='utf-8')
                print(result)
                output.write(result)
                output.close()
    
    gamelist = open("gamelist.txt", "w", encoding='utf-8')
    gamelist.close()
    
    return "\nDone."

def split(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

parser = argparse.ArgumentParser()
parser.add_argument("-p","--players",default='',help="Players (encase in double quotes and separate with commas)")
parser.add_argument("-pf","--playersfile",default='playerlist.txt',help="Player list file")
parser.add_argument("-o","--output",default='output.pgn',help="Output PGN file")

if __name__ == "__main__":
    args=parser.parse_args()
    print(main(args))

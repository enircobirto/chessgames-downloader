from multiprocessing import Process, Pool
import argparse

from getfromplayer import getfromplayer
from getfrompage import getfrompage
from alive_progress import alive_bar
from getgame import getgame
from pprint import pprint

def main(args):
    
    playerlist=[]
    
    try:
        playerlist = open(args.playersfile, "r").readlines()
        print("\n > File found.")
    except:
        print(" > Empty player file.")

    try:
        for player in args.players.split(','):
            playerlist.append(f'{player.strip()}\n')
        print(" > Arguments found.")
    except:
        if len(playerlist)==0:
            return " [ERROR] Empty player list! Run 'python main.py -h' for instructions."
        
    if(len(playerlist)==0):
        return " [ERROR] Empty player list! Run 'python main.py -h' for instructions."

    print(" > Players:")
    for line in playerlist:
        print(f' -> {line.strip()}')
    print('\n')
    n = min(len(playerlist),8)
    
    info = []

    spaces=""
    for i in range(0,len(args.output)):
        spaces+=' '
    
    with alive_bar(len(playerlist),title=f' > Extracting players {spaces}',bar='filling',spinner='classic') as bar:
       with Pool(n) as pool:
            for result in pool.imap_unordered(getfromplayer,playerlist):
                if result['pid']!='ERROR':
                    print(f"> {result['player']}({result['pid']}): {result['max']} pages")
                    info.append(result)
                    bar()
                else:
                    print(f"> Error getting info from {result['player']}")
    
    pagelist=[]
    for i in info:
        for num in range(1,i['max']):
            pagelist.append(dict({
                'player':i['player'],
                'pid':i['pid'],
                'page':num
            }))
    n = 16 

    with alive_bar(len(pagelist),title=f' > Extracting pages   {spaces}',bar='filling',spinner='classic') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(getfrompage,pagelist):
                bar()
    try:
        gamelist = open("gamelist", "r", encoding='utf-8').readlines()
    except:
        gamelist = open("gamelist", "w", encoding='utf-8')
        gamelist.close()
        gamelist = open("gamelist", "r", encoding='utf-8').readlines()

    with alive_bar(len(gamelist),title=f' > Exporting games to {args.output}',bar='filling',spinner='classic') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(getgame,gamelist):
                bar()
                output = open(args.output,"a+",encoding='utf-8')
                output.write(result)
                output.close()
    gamelist = open("gamelist", "w", encoding='utf-8')
    gamelist.close()
    
    return "\nDone."

parser = argparse.ArgumentParser()
parser.add_argument("-p","--players",help="Players (encase in double quotes and separate with commas)")
parser.add_argument("-pf","--playersfile",default='playerlist',help="Player list file (Default: playerlist)")
parser.add_argument("-o","--output",default='output.pgn',help="Output PGN file (Default: output.pgn)")

if __name__ == "__main__":
    args=parser.parse_args()
    print(main(args))

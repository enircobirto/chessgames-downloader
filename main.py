from getfromplayer import getfromplayer
from getgame import getgame
from alive_progress import alive_bar
from multiprocessing import Process, Pool
from pprint import pprint

def main():
    playerlist = open("playerlist.txt", "r")

    n = 5

    for player in playerlist.readlines():
        getfromplayer(player)

    gamelist = open("gamelist.txt", "r").readlines()
    section = list(split(gamelist,len(gamelist)//n))
    section.append(gamelist[:-len(gamelist)%n])

    with alive_bar(len(gamelist),title='Exporting games to result.pgn',bar='filling') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(getgame,gamelist):
                bar()
                print(result)

def work(gamelist):
    for game in gamelist:
        getgame(game)
        print("\n")

def split(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

if __name__ == "__main__":
    main()

from msvcrt import getch
from getfromplayer import getfromplayer
from getgame import getgame
from alive_progress import alive_bar
import threading

def main():
    playerlist = open("playerlist.txt", "r")
    
    # for player in playerlist.readlines():
        # getfromplayer(player)
    
    gamelist = open("gamelist.txt", "r").readlines()
    lists=list(split(gamelist,5))
    
    threads=[]
    
    for i in range(0,4):
        thread = threading.Thread(target=work(lists[i]), args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def work(gamelist):
    with alive_bar(len(gamelist),bar='filling') as bar:
        bar.title("Exporting games to result.pgn")
        for game in gamelist:
            getgame(game)
            bar()
def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]
if __name__ == "__main__":
    main()

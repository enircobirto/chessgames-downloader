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

    print(gamelist)
    getch()
    
    with alive_bar(len(gamelist),bar='filling') as bar:
        bar.title("Exporting games to result.pgn")
        for game in gamelist:
            getgame(game)
            bar()

if __name__ == "__main__":
    main()

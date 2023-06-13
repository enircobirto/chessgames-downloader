from getfromplayer import getfromplayer
from getgame import getgame
from alive_progress import alive_bar

def main():
    playerlist = open("playerlist.txt", "r")
    
    #for player in playerlist.readlines():
    #    getfromplayer(player)
    
    gamelist = open("gamelist.txt", "r").readlines()
    
    with alive_bar(len(gamelist),bar='filling') as bar:
        bar.title("Exporting games to result.pgn")
        result = open("result.pgn","w")
        for game in gamelist:
            result.write(getgame(game)+"\n")
            bar()

if __name__ == "__main__":
    main()
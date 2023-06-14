import argparse

from func.export_games import export_games
from func.get_page_list import get_page_list
from func.get_player_list import get_player_list
from func.player_info import player_info

parser = argparse.ArgumentParser()
parser.add_argument("-p","--players",help="Players (encase in double quotes and separate with commas)")
parser.add_argument("-pf","--playersfile",default='playerlist',help="Player list file (Default: playerlist)")
parser.add_argument("-o","--output",default='output.pgn',help="Output PGN file (Default: output.pgn)")

def main(args):
    playerlist = get_player_list(args)
    
    threads = 4
    spaces=""
    for i in range(0,len(args.output)):
        spaces+=' '

    info = player_info(playerlist,spaces,threads)

    threads = 16 
    get_page_list(info,spaces,threads)
    export_games(args.output,threads)
    
    return "\nDone."

if __name__ == "__main__":
    args=parser.parse_args()
    print(main(args))
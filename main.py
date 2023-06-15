import argparse

from func.export_games import export_games
from func.get_page_list import get_page_list
from func.get_player_list import get_player_list, EmptyPlayerList
from func.player_info import player_info

parser = argparse.ArgumentParser()
parser.add_argument("-p","--players",help="Players (encase in double quotes and separate with commas)")
parser.add_argument("-pf","--playersfile",default='playerlist',help="Player list file (Default: playerlist)")
parser.add_argument("-o","--output",default='output.pgn',help="Output PGN file (Default: output.pgn)")
parser.add_argument("--white-only",action='store_true')
parser.add_argument("--black-only",action='store_true')

def main(args):
    if args.white_only and args.black_only:
        return " > Please choose either '--white-only' or '--black-only'"
    try:
        playerlist = get_player_list(args)
    except EmptyPlayerList:
        return " > Program failed."

    threads = 4
    spaces=""
    for i in range(0,len(args.output)):
        spaces+=' '
    
    info = player_info(playerlist,spaces,threads)

    playerlist=[]

    for i in info:
        playerlist.append(i['player'])

    threads = 16 
    get_page_list(info,spaces,threads)
    
    options = {'white_only':args.white_only,'black_only':args.black_only}
    export_games(args.output,threads,options,spaces)
    
    return "\nDone."

if __name__ == "__main__":
    args=parser.parse_args()
    print(main(args))

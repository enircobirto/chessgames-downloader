def get_player_list(args):
    playerlist=[]
    try:
        playerlist = open(args.playersfile, "r").readlines()
    except:
        print(" > Empty player file.")

    try:
        for player in args.players.split(','):
            playerlist.append(f'{player.strip()}\n')
    except:
        if len(playerlist)==0:
            print (" [ERROR] Empty player list! Run 'python main.py -h' for instructions.")
            raise EmptyPlayerList
        
    if(len(playerlist)==0):
        print (" [ERROR] Empty player list! Run 'python main.py -h' for instructions.")
        raise EmptyPlayerList

    return playerlist

class EmptyPlayerList(Exception):
    """Player list is empty"""

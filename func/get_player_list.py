def get_player_list(args):
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
            print (" [ERROR] Empty player list! Run 'python main.py -h' for instructions.")
            raise EmptyPlayerList
        
    if(len(playerlist)==0):
        print (" [ERROR] Empty player list! Run 'python main.py -h' for instructions.")
        raise EmptyPlayerList

    print(" > Players:")
    for line in playerlist:
        print(f' -> {line.strip()}')
    print('\n')
    return playerlist

class EmptyPlayerList(Exception):
    """Player list is empty"""

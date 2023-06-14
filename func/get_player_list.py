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
            return " [ERROR] Empty player list! Run 'python main.py -h' for instructions."
        
    if(len(playerlist)==0):
        return " [ERROR] Empty player list! Run 'python main.py -h' for instructions."

    print(" > Players:")
    for line in playerlist:
        print(f' -> {line.strip()}')
    print('\n')
    return playerlist
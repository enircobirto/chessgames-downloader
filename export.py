import chess.pgn

def export(path):
    file = open("temp.pgn","r")

    game = chess.pgn.read_game(file)
    i=0
    while game != None:
        new_pgn = open(path,"a")
        game = chess.pgn.read_game(file)
        if game != None:
            new_pgn.write(str(game))
            new_pgn.write('\n\n\n')
        new_pgn.close()
        i+=1

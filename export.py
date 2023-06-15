import chess.pgn

def export(path):
    file = open("temp.pgn","r")

    while True:
        game = chess.pgn.read_game(file)
        if game == None:
            break
        new_pgn = open(path,"a")
        new_pgn.write(str(game))
        new_pgn.write('\n\n\n')
        new_pgn.close()

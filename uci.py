"""
UCI Compliance 
https://page.mi.fu-berlin.de/block/uci.htm

In Progress
"""
import sys
import chess
from ChessAI import *

def send(str):
    """
    Use instead of print for UCI essential messages.
    """
    print(str)

def uci(ai):
    """
    UCI initialization and commands 
    """
    board = chess.Board()

    while True:
        # stdin commands and params
        uci_cmd = input().strip()
        uci_params = uci_cmd.split(" ")

        if uci_cmd == "uci":
            send("id name chessai")
            send("id author leesamuel423")
            send("uciok")

        elif uci_cmd == "isready":
            send("readyok")

        elif uci_cmd == "ucinewgame":
            board = chess.Board()
        
        elif uci_cmd == "quit":
            sys.exit()

        elif uci_cmd == "print":
            print(board)

        elif uci_cmd.startswith("position"):
            """Set up the position described in fenstring on the internal board and play the moves on the internal chess board.
            If the game was played from the start postion the string "startpos" will be sent. Note: no "new" command is needed.""" 
            """ie: """
            # FEN Handling 
            if uci_params[1] == "fen":
                FEN = uci_params[2]
            elif uci_params[1] == "startpos":
                send("startpos")
                FEN = chess.STARTING_FEN
            else:
                raise SyntaxError("ERROR: UCI Syntax")

            # MOVES Handling
            moves_index = uci_cmd.find("moves")
            moves = [] # list of moves

            if moves_index >= 0:
                moves = uci_cmd[moves_index:].split()[1:]
            board = chess.Board(FEN)
            for move in moves:
                board.push_uci(move)
                print(board)
        
        elif uci_cmd.startswith("go"):
            #TODO: add the rest of the funtionality
            best_move = ai.select_best_move(board) 
            send(f'Best Move: {best_move}')
            return (best_move, None)


if __name__ == "__main__":
    ai = ChessAI()
    uci(ai)


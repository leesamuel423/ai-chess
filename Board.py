import chess


class Board():
    def __init__(self, fen = None):
        if not fen:
            self.board = chess.Board()
        else:
            # if FEN provided, start with FEN
            self.board = chess.Board(fen)



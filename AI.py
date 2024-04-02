import chess
import chess.syzygy
from heuristics.pesto_heuristics import *
from endgame.endgames import *

class AI:
    def __init__(self):
        """Initialize Chess AI"""
        pass

    def eval(self, board):
        """
        Evaluate current board and return score
        If piece count is less than 5, use Syzygy Endgame Table
        """
        # Syzygy Endgame
        syzygy = db_check(board)

        return syzygy if syzygy is not None else self.pesto_eval(board)

    def pesto_eval(self, board):
        return 100

if __name__ == "__main__":
    ai = AI()
    board = chess.Board("K7/5NN1/8/8/8/8/p7/7k w - - 0 1")
    # board = chess.Board("K7/5NN1/3r4/8/8/2Q5/p7/7k w - - 0 1")
    eval1 = ai.eval(board)
    print(eval1)


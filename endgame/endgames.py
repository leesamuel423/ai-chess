import chess.syzygy

PATH = 'endgame/syzgy-3-4-5'

def db_check(board):
    pieces = len(board.piece_map())

    if pieces <= 5:
        tablebase = chess.syzygy.open_tablebase(PATH)
        return tablebase.probe_dtz(board)

# Note: Implemenet care for 50 move rule -> Wasting moves?

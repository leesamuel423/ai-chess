import chess
import chess.svg
import sys
from Display import *
from PyQt6.QtWidgets import QApplication


def main():
    # Prompt for FEN
    FEN = input('Press Enter to Begin or Add a Valid FEN: ')

    # FEN Validation
    try:
        board = chess.Board(FEN)
    except:
        board = chess.Board()


    app = QApplication([])
    window = Display()
    chessboardSvg = chess.svg.board(board, flipped = True).encode("UTF-8")
    window.widgetSvg.load(chessboardSvg)
    window.show()
    app.processEvents()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()

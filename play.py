import chess
import chess.svg
import sys
from Display import *
from PyQt6.QtWidgets import QApplication


def main():
    # Prompt for starting color (default white)
    starting_color = input('Select (W)hite or (B)lack: ')

    # Validation (starting color)
    if starting_color and starting_color[0].lower() == "b":
        starting_color = True
    else:
        starting_color = False


    # Prompt for FEN
    FEN = input('Press <Enter> to Begin or Input FEN: ')

    # Validation (FEN)
    try:
        board = chess.Board(FEN)
    except:
        board = chess.Board()

    # Initialize QApplication (required for PyQt apps)
    app = QApplication([])
    # Convert chess board into SVG and encode it to UTF-8 for displaying
    chessboardSvg = chess.svg.board(board, flipped = starting_color).encode("UTF-8")
    # Create Display window instance
    window = Display()
    window.widgetSvg.load(chessboardSvg)
    window.show()
    # Process any pending events for app
    app.processEvents()

    # Execute app and exit window when user closes window
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

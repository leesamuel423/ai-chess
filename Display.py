import chess
import chess.svg
import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QShortcut, QKeySequence

print("in Display")

class Display(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess")
        
        # initialize window: top-left corner 1000 x 1000
        self.setGeometry(0, 0, 1000, 1000)

        self.widgetSvg = QSvgWidget(parent = self)
        self.widgetSvg.setGeometry(0, 0, 1000, 1000)

        self.chessboard = chess.Board()
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8") 
        self.widgetSvg.load(self.chessboardSvg)
        self.shortcuts()

    def shortcuts(self):
        # close window
        self.shortcut_close = QShortcut(QKeySequence('Ctrl+W'), self)
        self.shortcut_close.activated.connect(self.close)



board = chess.Board()

if __name__ == "__main__":
    app = QApplication([])
    window = Display()
    chessboardSvg = chess.svg.board(board, flipped = True).encode("UTF-8")
    window.widgetSvg.load(chessboardSvg)
    window.show()
    app.processEvents()
    sys.exit(app.exec())

import chess
import chess.svg

from PyQt6.QtWidgets import QWidget
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QShortcut, QKeySequence

class DisplayWindow(QWidget):

    def __init__(self):
        # Call initializer of base class QWidget to setup window correctly
        super().__init__()
        self.setWindowTitle("Chess")
        
        # Initialize window: top-left corner w/ size 1000 x 1000
        self.setGeometry(0, 0, 1000, 1000)

        # Create SVG widget to display chess pieces/board and set geometry to fill window
        self.widgetSvg = QSvgWidget(parent = self)
        self.widgetSvg.setGeometry(0, 0, 1000, 1000)

        # Initialize starting color and FEN
        self.starting_color = self.startingSide()
        self.board = self.startingFEN()

        # Convert chess board into SVG and encode it to UTF-8 for displaying
        self.chessboardSvg = chess.svg.board(self.board, flipped = self.starting_color).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

        self.shortcuts()


    def startingSide(self):
        """
        Prompt for starting color and return boolean
        to be used when converting chess board into SVG
        """
        starting_color = input('Select (W)hite or (B)lack: ')

        # Validation (starting color)
        return True if starting_color and starting_color[0].lower() == "b" else False
        

    def startingFEN(self):
        """
        Prompt for starting FEN and return chess.Board() instance initialized
        with proper FEN
        """
        FEN = input('Press <Enter> to Begin or Input FEN: ')

        # Validation (FEN)
        try:
            return chess.Board(FEN)
        except:
            return chess.Board()

    
    def shortcuts(self):
        """
        Shortcuts for Window
        <Ctrl + W> close window
        <Ctrl + M> minimize window
        """
        # Close window
        self.shortcut_close = QShortcut(QKeySequence('Ctrl+W'), self)
        self.shortcut_close.activated.connect(self.close)

        # Minimize window
        self.shortcut_minimize = QShortcut(QKeySequence('Ctrl+M'), self)
        self.shortcut_minimize.activated.connect(self.showMinimized)


    def clickEvent(self, e):
        """
        Handle left mouse click and allow moving chess pieces by clicking
        on piece and then target square.
        """
        pass        


    def moveValidation(self, e):
        """
        Validates that user is trying to do a valid move.
        """
        pass


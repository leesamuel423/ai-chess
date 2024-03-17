import chess.svg

from PyQt6.QtWidgets import QWidget
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QShortcut, QKeySequence

class Display(QWidget):
    def __init__(self):
        # Call initializer of base class QWidget to setup window correctly
        super().__init__()
        
        self.setWindowTitle("Chess")

        
        # Initialize window: top-left corner w/ size 1000 x 1000
        self.setGeometry(0, 0, 1000, 1000)

        # Create SVG widget to display chess pieces/board and set geometry to fill window
        self.widgetSvg = QSvgWidget(parent = self)
        self.widgetSvg.setGeometry(0, 0, 1000, 1000)

        self.shortcuts()
        
    
    def shortcuts(self):
        '''Shortcuts for Window
        <Ctrl + W> close window
        <Ctrl + M> minimize window
        '''
        # Close window
        self.shortcut_close = QShortcut(QKeySequence('Ctrl+W'), self)
        self.shortcut_close.activated.connect(self.close)

        # Minimize window
        self.shortcut_minimize = QShortcut(QKeySequence('Ctrl+M'), self)
        self.shortcut_minimize.activated.connect(self.showMinimized)

import chess.svg

from PyQt6.QtWidgets import QWidget
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QShortcut, QKeySequence

class Display(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess")

        
        # initialize window: top-left corner 1000 x 1000
        self.setGeometry(0, 0, 1000, 1000)

        self.widgetSvg = QSvgWidget(parent = self)
        self.widgetSvg.setGeometry(0, 0, 1000, 1000)

        self.shortcuts()
        
    
    def shortcuts(self):
        '''Shortcuts for Window
        <Ctrl + W> close window
        <Ctrl + M> minimize window
        '''
        # close window
        self.shortcut_close = QShortcut(QKeySequence('Ctrl+W'), self)
        self.shortcut_close.activated.connect(self.close)

        self.shortcut_minimize = QShortcut(QKeySequence('Ctrl+M'), self)
        self.shortcut_minimize.activated.connect(self.showMinimized)

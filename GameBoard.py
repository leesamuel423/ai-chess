import chess
import chess.svg

from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtCore import Qt

class GameBoard(QWidget):

    def __init__(self):
        """Initialize chess game board and UI components"""
        super().__init__() # call initializer of base class QWidget to setup window correctly

        self.setWindowTitle("Chess")
        self.setGeometry(0, 0, 1000, 1000)

        self.setupBoard()
        self.setupUI()
        # Variables for Tracking Game State
        self.pieceToMove = [None, None] # track piece selected for moving
        self.starting_color = self.startingSide() # starting color
        self.board = self.startingFEN() # starting FEN
        self.lastMove = None # last move made
        self.possibleMoves = [] # possible moves for selected piece
        self.redoStack = [] # stack to hold moves for redo

        self.drawBoard() # chess board visualization

    def setupBoard(self):
        """Set up the chess board display using SVG widget"""
        # Chess board display setup
        self.widgetSvg = QSvgWidget(parent = self)
        self.widgetSvg.setGeometry(10, 10, 700, 700)

        # Calculating size and margins for chessboard display
        self.boardSize = min(self.widgetSvg.width(), self.widgetSvg.height())
        self.coordinates = True # show coordinates around chess board
        self.margin = 0.05 * self.boardSize if self.coordinates else 0
        self.squareSize = (self.boardSize - 2 * self.margin) / 8.0 # size of each board square

    def setupUI(self):
        """Set up the UI components including labels and shortcuts"""
        # UI for game status
        self.turnLabel = QLabel("Turn: White", parent=self) # display which player turn it is
        self.turnLabel.setGeometry(720, 10, 200, 30)
        self.shortcuts() # keyboard shortcuts


    def startingSide(self):
        """Selection of starting color"""
        starting_color = input('Select (W)hite or (B)lack: ')
        return True if starting_color and starting_color[0].lower() == "b" else False
        

    def startingFEN(self):
        """Selection of starting FEN or default FEN"""
        FEN = input('Press <Enter> to Begin or Input FEN: ')

        # Validation (FEN)
        try:
            return chess.Board(FEN)
        except:
            return chess.Board()


    def drawBoard(self):
        """Draw chess board w/ current game state and check for game end"""
        self.chessboardSvg = chess.svg.board(self.board, 
            lastmove=self.lastMove,
            squares = self.possibleMoves,
            flipped = self.starting_color
        ).encode("UTF-8")
        
        self.widgetSvg.load(self.chessboardSvg)

        self.updateTurnLabel()
        self.checkGameEnd()

    def updateTurnLabel(self):
        """Update the label indicating whose turn it is"""
        # Update turn label
        turn_text = "Turn: " + ("Black" if self.board.turn == chess.BLACK else "White")
        self.turnLabel.setText(turn_text)


    def checkGameEnd(self):
        """Check for game-ending conditions and display a message if the game has ended."""
        if self.board.is_checkmate():
            winner = "Black" if self.board.turn == chess.WHITE else "White"
            self.turnLabel.setText("Game Over ... " + f"Checkmate!\n{winner} wins.")
        elif self.board.is_stalemate():
            self.turnLabel.setText("Game Over ... " + "Stalemate!\nThe game is a draw.")
        elif self.board.is_insufficient_material():
            self.turnLabel.setText("Game Over!" + "\nDraw due to insufficient material.")
        elif self.board.is_seventyfive_moves():
            self.turnLabel.setText("Game Over!" + "\nDraw due to 75-move rule.")
        elif self.board.is_fivefold_repetition():
            self.turnLabel.setText("Game Over!" + "\nDraw due to fivefold repetition.")
        elif self.board.is_variant_draw():
            self.turnLabel.setText("Game Over!" + "\nDraw due to variant-specific reason.")

    def pawnPromotion(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Pawn Promotion")
        dialog.setText("Choose piece for promotion: ")

        # Custom buttons for each promotion choice
        queenButton = dialog.addButton("Queen", QMessageBox.ButtonRole.YesRole)
        rookButton = dialog.addButton("Rook", QMessageBox.ButtonRole.YesRole)
        bishopButton = dialog.addButton("Bishop", QMessageBox.ButtonRole.YesRole)
        knightButton = dialog.addButton("Knight", QMessageBox.ButtonRole.YesRole)

        dialog.exec()

        # Return the chosen piece
        if dialog.clickedButton() == queenButton:
            return chess.QUEEN
        elif dialog.clickedButton() == rookButton:
            return chess.ROOK
        elif dialog.clickedButton() == bishopButton:
            return chess.BISHOP
        elif dialog.clickedButton() == knightButton:
            return chess.KNIGHT
        else:
            return chess.QUEEN  # Default to queen
        
    
    def shortcuts(self):
        """Keyboard shortcuts for window operations
        <Ctrl + W> close window
        <Ctrl + M> minimize window
        <Ctrl + Z> undo last move
        """
        # Close window
        self.shortcut_close = QShortcut(QKeySequence('Ctrl+W'), self)
        self.shortcut_close.activated.connect(self.close)

        # Minimize window
        self.shortcut_minimize = QShortcut(QKeySequence('Ctrl+M'), self)
        self.shortcut_minimize.activated.connect(self.showMinimized)

        # Undo Last Move
        self.shortcut_undo = QShortcut(QKeySequence('Ctrl+Z'), self)
        self.shortcut_undo.activated.connect(self.undoMove)

        # Redo Last Move
        self.shortcut_redo = QShortcut(QKeySequence('Ctrl+Y'), self)
        self.shortcut_redo.activated.connect(self.redoMove)


    def mousePressEvent(self, e):
        """Handle mouse press events for selecting and moving chess pieces."""
        # Get positions of mouse click
        pos = e.position()
        x, y = pos.x(), pos.y()
        
        # Check if left mouse button was pressed in board bounds
        if e.button() == Qt.MouseButton.LeftButton and x <= self.boardSize and y <= self.boardSize:
            # Adjust file and rank calculation based on whether the board is flipped
            if self.starting_color:  # If starting color is True (black), then the board is flipped
                file = 7 - int((x - self.margin) / self.squareSize)
                rank = int((y - self.margin) / self.squareSize)
            else:
                file = int((x - self.margin) / self.squareSize)
                rank = 7 - int((y - self.margin) / self.squareSize)
            # EDGE CASE: If file is not in valid 0-7 range, return
            if file < 0 or file > 7 or rank < 0 or rank > 7:
                return

            # Convert the file and rank to a square in the chess library's notation
            square = chess.square(file, rank)
            coordinates = "{}{}".format(chr(file + 97), str(rank + 1))
            
            # Check if piece is already selected for moving
            if self.pieceToMove[1] is not None:
                # Check if current click is in a different square than initial position
                if self.pieceToMove[1] != coordinates:

                    # Create move in UCI format
                    move = chess.Move.from_uci(f"{self.pieceToMove[1]}{coordinates}")

                    #Check for pawn promotion
                    if (self.board.piece_at(move.from_square).piece_type == chess.PAWN and (move.to_square >= chess.A8 or move.to_square <= chess.H1)):
                        promotion_choice = self.pawnPromotion()  # Prompt for pawn promotion
                        move = chess.Move(move.from_square, move.to_square, promotion=promotion_choice)

                    # If move is valid...
                    if move in self.board.legal_moves:
                        self.board.push(move) # make move on board
                        self.lastMove = move # update last move state
                        self.possibleMoves = [] # clear possible moves
                        self.redoStack = [] # clear redo stack b/c new moves invalidate it
                    else:
                        # If move isn't legal, highlight possible moves for piece
                        self.possibleMoves = [move.to_square for move in self.board.legal_moves if move.from_square == square]
                else:
                    # Deselect piece if clicked square is same as selected piece square
                    self.possibleMoves = []
                self.pieceToMove = [None, None]
            else:
                # If no piece selected and clicked square has a piece, select that piece and show possible moves
                piece = self.board.piece_at(square)
                if piece:
                    self.pieceToMove = [piece, f"{chr(file + 97)}{str(rank + 1)}"]
                    self.possibleMoves = [move.to_square for move in self.board.legal_moves if move.from_square == square]
                else:
                    # If clicked square doesn't have piece, clear possiblities
                    self.possibleMoves = []

            # Redraw board to reflect changes
            self.drawBoard()


    def undoMove(self):
        """Undo last move and update game state"""
        if len(self.board.move_stack) > 0:
            # Add last move to redo stack before undoing it
            self.redoStack.append(self.board.pop())
            # If there was a last move, update it to the new last move if any
            self.lastMove = self.board.peek() if len(self.board.move_stack) > 0 else None
            # Clear possible moves as the selection is now potentially invalid
            self.possibleMoves = []
            # Reset piece to move
            self.pieceToMove = [None, None]
            # Redraw the board with the updated state
            self.drawBoard()
    
    def redoMove(self):
        """Redo last move and update game state"""
        if len(self.redoStack) > 0:
            # If there is move in redoStack, pop it and add to board
            move = self.redoStack.pop()
            self.board.push(move)
            # Update state
            self.lastMove = move
            # Clear possible moves as the selection is now potentially invalid
            self.possibleMoves = []
            # Reset piece to move
            self.pieceToMove = [None, None]
            # Redraw the board with the updated state
            self.drawBoard()


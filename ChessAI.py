import chess
from heuristics import *

class ChessAI:

    def __init__(self, depth=3, ai_color=chess.WHITE):
        """
        Initialize Chess AI

        @param depth: depth for the minimax search algorithm
        @param ai_color: color this AI will play as, chess.WHITE or chess.BLACK
        """
        self.depth = depth
        self.color = ai_color
        self.last_piece_moved = None  # Track the last piece moved by the AI for potential future enhancements.

    def evaluate_board(self, board):
        """
        Evaluates the board using material and positional heuristics.

        @param board: chess board to evaluate
        @return: numerical evaluation of board's state from the perspective of the AI's color. (+) favorable, (-) unfavorable
        """
        if board.is_checkmate():
            return -9999 if board.turn else 9999
        if board.is_stalemate():
            return 0
        if board.is_insufficient_material():
            return 0
        
        eval = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                piece_type = piece.piece_type
                color = piece.color
                value = 0
                
                # Determine the piece's base value and position value
                if piece_type == chess.PAWN:
                    value = 100 + self.get_position_value(piece_type, square, color, board)
                elif piece_type == chess.KNIGHT:
                    value = 320 + self.get_position_value(piece_type, square, color, board)
                elif piece_type == chess.BISHOP:
                    value = 330 + self.get_position_value(piece_type, square, color, board) 
                elif piece_type == chess.ROOK: 
                    value = 500 + self.get_position_value(piece_type, square, color, board)
                elif piece_type == chess.QUEEN:
                    value = 900 + self.get_position_value(piece_type, square, color, board)
                elif piece_type == chess.KING:
                    value = 20000 + self.get_position_value(piece_type, square, color, board)

                # Adjust the score based on the piece's color
                eval += value if color == self.color else -value

        mobility = mobility_score(board)
        eval += mobility if board.turn == self.color else -mobility

        return eval

    def get_position_value(self, piece_type, square, color, board):
        """
        Returns the position value of a piece based on its type and square.
        @param piece_type: type of the chess piece
        @param square: square where the piece is located on the board
        @param color: color of piece (chess.WHITE or chess.BLACK)
        @param board: board state
        @return: heuristic value of piece at the given square
        """
        endGame = endgame_check(board)
        piece_key = ''
        if piece_type == chess.KING:
            piece_key = 'kingStart' if not endGame else 'kingEnd'
        elif piece_type == chess.PAWN:
            piece_key = 'pawns' if not endGame else 'pawnsEnd'
        elif piece_type == chess.ROOK:
            piece_key = 'rooks'
        elif piece_type == chess.KNIGHT:
            piece_key = 'knights'
        elif piece_type == chess.BISHOP:
            piece_key = 'bishops'
        else:
            piece_key = 'queen'

        table = materialHeuristics[piece_key]
        if color == chess.BLACK:
            table = list(reversed(table))  # Reverse table for black pieces
        return table[square]

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        """
        Implement minimax algorithm with alpha-beta pruning w/ fail-soft

        @param board: current board state
        @param depth: current depth in the search tree
        @param alpha: alpha value for pruning
        @param beta: beta value for pruning
        @param maximizing_player: Boolean indicating if current player is maximizing or minimizing the score
        @return: best evaluation score for current board position and depth
        """
        # Base Case: return board eval if max depth is reached or game over
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board)

        if maximizing_player:
            max_eval = -float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval) #fail soft alpha update
                # alpha-beta pruning
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval) # fail-soft beta update
                # alpha-beta pruning
                if beta <= alpha:
                    break
            return min_eval

    def select_best_move(self, board):
        """
        Selects the best move for the AI based on the current board state

        @param board: current board state
        @return: best move determined by minimax
        """
        best_move = None
        best_value = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            # evaluate move
            move_value = self.minimax(board, self.depth - 1, -float('inf'), float('inf'), False)
            board.pop()

            if move_value > best_value:
                best_value = move_value
                best_move = move

        return best_move

    

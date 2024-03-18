# Notes
- DB lichess


## Pieces (BINARY REPRESENTATION)
- Can represent pieces as binaries (5 places) where first 2 represent black or white and last 3 represent type of pieces
- Blank (0)
- Pawn (1)
- Rook (2)
- Knight (3)
- Bishop (4)
- Queen (5)
- King (6)
- White (8)
- Black (16)

ie: black rook = 16 + 2 = 18 -> 10010
    white rook = 8 + 2 = 10 -> 01010

## Chessboard
- x (row), y (column)
- light, dark
- can determine whether (x, y) position is light/black via 
(x + y) & 1 -> dark

- Squares by default piece 0

## FEN-(Forsynth Edwards Notation)[https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation] Strings
- notation for representing board positions of chess game
- White Pieces (PNBRQK), Black Pieces (pnbrqk), w (white active color), b (black active color)
- empty spaces (1-8) in rank, "/" to denote next rank
- neither side can castle and no en passant target square "-"
- Fifty-move rule (https://en.wikipedia.org/wiki/Fifty-move_rule) -> half move clock
- Fullmove clock (incremented after black's move)

ie:
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
-> FEN for starting position

## (chess.svg)[https://python-chess.readthedocs.io/en/latest/svg.html]


## MinMax Algo
- Minmax is backtracking algo to find optimal move (assuming opponent plays optimally)
    - maybe will find edge cases from non-optimal opponent
- Two players: Maximizer -> highest score possible, Minimizer -> Lowest score possible
- Board states have values associated with it --> TODO create board states with values
    - if maximizer has upper hand, board state is positive, if minimizer, negative
    - board values calculated by heuristics
- alpha beta pruning happens when we get rid of computation if it won't affect the outcome regardless
    - order of the moves should be ordered from best to worst for the player whose turn it is.
    - order moves on how likely it is to be good
        - ie: capturing piece w/ pawn is likely to be good, so explore it first

## TODO
-[x] Load/Display gui
-[x] Load positions with FEN
-[x] Set orientations
-[] Move QApplication code to display as well???
-[] make chessboard scale with window
-[] user interaction with gui to move pieces
-[] user move validation
-[] indicators to show valid moves
    -[] check whether indicators show edge cases (EnPassant, Castle, Promotion)
-[] make sure valid fen is retrieved per move

-[] Look into alpha-beta pruning algorithm
-[] Create Board heuristics


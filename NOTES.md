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


## TODO
-[] chessboard state
-[x] Load positions with FEN
-[] Valid Moves


# Notes
- DB lichess
- [FEN Examples](https://github.com/zabuzara/Chess-Fen/blob/main/FENs.txt)
- "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" -> FEN for starting position

## MinMax Algo
- Minmax is backtracking algo to find optimal move (assuming opponent plays optimally)
    - maybe will find edge cases from non-optimal opponent
- Two players: Maximizer -> highest score possible, Minimizer -> Lowest score possible
- Board states have values associated with it --> TODO create board state heuristics
    - if maximizer has upper hand, board state is positive, if minimizer, negative
    - board values calculated by heuristics
- alpha beta pruning happens when we get rid of computation if it won't affect the outcome regardless
    - order of the moves should be ordered from best to worst for the player whose turn it is.
    - order moves on how likely it is to be good
        - ie: capturing piece w/ pawn is likely to be good, so explore it first
- fail-soft vs fail-hard alpha beta pruning
    - fail-soft pruning allows alpha or beta values to be updated even if current node's values is outside the [alpha, beta] range. Potentially allows for more aggressive pruning and thus better performance for pruning efficiency.
    - fail-hard pruning strictly updates alpha and beta values only when current node's value is strictly greater than alpha or strictly less than beta. Potentially leads to less efficient pruning because exact value of a node outside [alpha, beta] range is not used. However, better memory usage.

## Heuristics
considerations:
- Material: encourage AI to capture pieces and make favorable plays
    - pawn (1), bishop(3), knight(3), rook(5), queen(9)
- pawn structure: AI should develop pawns to control center and defend each other
- Checkmates: look for checkmates (highest priority)
    - Similarly, chekc situations would also be good
- King safety: look for castling and placing kings in corners in early mid game
    - end game, we should look to use king in support of promotions and attack, so use two heuristics for early, mid, end game
- Center control
- [Killer Heuristic](https://en.wikipedia.org/wiki/Killer_heuristic) for alpha-beta pruning efficiency

## TODO
- [x] Load/Display gui
- [x] Load positions with FEN
- [x] Set orientations
- [x] Move QApplication code to display as well???
- [x] user interaction with gui to move pieces
- [x] FIX:when orientation flipped for black, user input does not also reverse
- [x] user move validation
- [x] indicators to show valid moves
    - [x] check whether indicators show edge cases (EnPassant, Castle, Promotion)
- [x] Address pawn promotion
- [x] check to see if game ends and show who won
- [x] show whose turn it is
- [x] show FEN

- [x] Look into alpha-beta pruning algorithm
- [x] Create Board heuristics


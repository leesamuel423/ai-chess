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
- [ ] Address pawn promotion
- [x] check to see if game ends and show who won
    - [ ] new game option
- [x] show whose turn it is
- [x] show FEN

- [ ] Look into alpha-beta pruning algorithm
- [ ] Create Board heuristics

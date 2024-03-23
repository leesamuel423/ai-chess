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
- conversion into UCI (https://github.com/thomasahle/sunfish)
- bratko-kopec testing (https://www.chessprogramming.org/Bratko-Kopec_Test)
- implementation of Pesto Eval func w/ Tapered Eval
- organize move ordering for better alpha-beta pruning
- multiprocessing?

- host on lichess

- add openings w/ Cerebellum
- add endgame syzygy

## Test Positions
- [ ] Checkmate Position
    - Play as Black
    - FEN: r1bqkb1r/pppppppp/8/1n6/1n6/1B2PQ2/PPPP1PPP/R1B1K1NR w KQkq - 0 7
    - Expected Behavior: Queen Takes and Checkmate OR Bishop Takes and Checkmate

- [ ] Optimal take (SEE implementation)
    - Play as White
    - FEN: r1b1kb1r/pppp1ppp/2n1pq2/8/4P3/3P1Q2/PPP2PPP/RN2KBNR b KQkq - 1 5
    - Expected Behavior: Queen takes free pawn rook side and threatens rook take

- [ ] Queen Valuation
    - Play as White
    - FEN: rnb1kbnr/pppp1ppp/8/4p3/4PP1q/6P1/PPPP3P/RNBQKBNR b KQkq - 0 3
    - Expected Behavior: Prioritize protecting queen

- [ ] Rook Shuffle
    - Play as White
    - FEN: r6r/pppk1ppp/4p3/3b4/1PP1N2q/5P2/5NPP/R2QR1K1 b - - 0 19
    - FEN: 3rkb1r/ppp1pppp/8/3P4/1PP5/P2N1PP1/7P/R3R1K1 b - - 0 21
    - Expected Behavior: Anything useful, why rook shuffle?

- [ ] King Endgame Play
    - Play as White
    - FEN:  r3kb1r/ppp1pppp/2p5/8/1PbPP2q/P4P2/2P2NPP/RN1QR1K1 b kq - 7 13
r3kb1r/ppp1pppp/2p5/8/1PbPP2q/P4P2/2P2NPP/RN1QR1K1 b kq - 7 13
    - Expected Behavior: Maybe castling? Why is King moving forward as if endgame condition has been met?

# AI Chess

Chess AI utilizing minmax algorithm with alpha-beta pruning (fail-soft), enhanced with heuristics for piece valuation and positional play. Developed with PyQt6 for graphical user interface.

## Heuristics:
The AI employs several heuristic evaluations to improve its gameplay, making decisions based on a variety of factors:
- Material Positions: Evaluates the position of pieces on the board, taking into account their control over key squares and potential for movement.
- Material Balance: Considers the total value of pieces for both players, guiding the AI in material exchanges and captures.
- Game Stage: Adapts strategy based on the phase of the game (opening/midgame, endgame), optimizing piece placement and prioritizing goals appropriate to each stage.


## Installation
Ensure you have Python 3.8+ and pip installed on your system. Follow these steps to set up the game:

1. Clone the Project Repository
Make sure you have Python 3.8+ installed on your system. Clone the repository using the following command:
```bash
git clone https://your-repository-link.git
cd ai-chess
```

2. Create and Activate a Virtual Environment
A virtual environment is recommended to keep dependencies required by the project separate and to avoid any conflicts with other projects. Create a virtual environment by running:
```bash
# For Unix or MacOS
python3 -m venv venv

# For Windows
python -m venv venv
```

Activate the virtual environment with:
```bash
# For Unix or MacOS
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

3. Install Required Python Packages
Install all dependencies specified in the `requirements.txt` file using pip:
```bash
pip install -r requirements.txt
```
This command ensure that all the required Python packages, such as PyQt6 and python-chess, are installed in your virtual environment

4. Running the Game
Start the game with the following command:
```bash
python play.py
```
You will be prompted to select:
    - Initial side (W)hite or (B)lack
    - FEN (can input a custom FEN or default to initial board)
        - Example FEN: r1b1kb1r/pppp1ppp/2n1pq2/8/4P3/3P1Q2/PPP2PPP/RN2KBNR b KQkq - 1 5


## Contributing
Contributions are welcome. Below are known issues that need to be resolved
- [ ] UI Bug: When capturing AI piece, sometimes buggy
- [ ] AI: Shuffling pieces
- [ ] AI: Static Exchange Evaluation implementation
- [ ] AI: Castling priority
- [ ] AI: Early evaluation of endgame?

Testing can be done utilizing the following command:
```bash
pytest [[file_name]]
```


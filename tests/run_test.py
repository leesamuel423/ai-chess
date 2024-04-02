import pytest
import time
import chess
from ChessAI import *

class TestChess():
    def process_file(self, file):
        print(f"Processing {file}")
        with open(file) as f:
            file_lines = f.readlines()

        tests = []
        for line in file_lines:
            params = line.strip().split(" - ")
            best_moves = params[1].split("bm ")[1].split(";")[0].split(' ')
            tests.append((params[0], best_moves))

        return tests

    @pytest.mark.parametrize("suite, file", [
        ("BK", "tests/bk.txt"),
        # ("WAC", "tests/wac.txt"),
    ])
    def test_suite(self, suite, file):
        print(f".... Testing {suite} ....")
        tests = self.process_file(file)
        ai = ChessAI()

        correct = 0
        start_time = time.monotonic()

        for i, (fen, best_moves) in enumerate(tests):
            board = chess.Board(fen)
            result = ai.select_best_move(board)
            if result in best_moves:
                correct += 1
                print("✅", str(i) + ":", result)
            else:
                print("❌", str(i) + ":", result)
        end_time = time.monotonic()
        print(f"SUMMARY:\ntime: {end_time - start_time}\n correct: {correct}/{len(tests)}")

if __name__ == "__main__":
    tests = TestChess()
    print(tests.test_suite("BK", "tests/bk.txt"))
    print(tests.test_suite("WAC", "tests/wac.txt"))

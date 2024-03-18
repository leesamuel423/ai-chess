import pytest
from unittest.mock import patch
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtTest import QTest
from GameBoard import GameBoard

@pytest.fixture
def display_widget(request):
    """
    Fixture to create and return a Display widget with a patched 'input' value.
    The request.param will dictate the behavior for 'input' return values.
    """
    input_values = request.param
    with patch('builtins.input', side_effect=input_values):
        widget = GameBoard()
        widget.show()
        yield widget

# Test default behavior
@pytest.mark.parametrize('display_widget', [(['', ''])], indirect=True)
def test_starting_white_default_FEN(display_widget, qtbot):
    """
    Test that the default behavior is 
    FEN defaulted to the standard opening and starting with white.
    """
    expected_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    assert display_widget.board.fen() == expected_fen
    assert display_widget.starting_color == False # False indicates white

# Test starting with black
@pytest.mark.parametrize('display_widget', [(['B', ''])], indirect=True)
def test_starting_black_default_FEN(display_widget, qtbot):
    """
    Test that the initial FEN is correctly set when starting with black.
    """
    assert display_widget.starting_color == True  # True indicates black

# Test with a different, valid FEN
@pytest.mark.parametrize('display_widget', [(['', '7R/k1p5/8/2n1p3/3N1r2/1b6/1Knr4/b1q5 w - - 4 9'])], indirect=True)
def test_custom_FEN(display_widget, qtbot):
    """
    Test that the board is initialized with a custom FEN correctly.
    """
    expected_fen = "7R/k1p5/8/2n1p3/3N1r2/1b6/1Knr4/b1q5 w - - 4 9"
    assert display_widget.board.fen() == expected_fen

# Test with an invalid FEN
@pytest.mark.parametrize('display_widget', [(['', 'invalid FEN string'])], indirect=True)
def test_invalid_FEN(display_widget, qtbot):
    """
    Test that the board falls back to the default FEN when given an invalid FEN.
    """
    expected_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"  # Default FEN
    assert display_widget.board.fen() == expected_fen

# Test Ctrl+W
@pytest.mark.parametrize('display_widget', [(['', ''])], indirect=True)
def test_close_shortcut(display_widget, qtbot):
    """
    Test that the Display widget closes when the Ctrl+W shortcut is used.
    """
    assert display_widget.isVisible() == True
    QTest.keyPress(display_widget, Qt.Key.Key_W, Qt.KeyboardModifier.ControlModifier)
    QApplication.processEvents()
    assert display_widget.isVisible() == False

# Test Ctrl+M
@pytest.mark.parametrize('display_widget', [(['', ''])], indirect=True)
def test_minimize_shortcut(display_widget, qtbot):
    """
    Test that the Display widget minimizes when the Ctrl+M shortcut is used.
    """
    assert display_widget.isVisible() == True
    QTest.keyPress(display_widget, Qt.Key.Key_M, Qt.KeyboardModifier.ControlModifier)
    QApplication.processEvents()
    assert display_widget.isMinimized() == True

@pytest.mark.parametrize('display_widget', [(['', ''])], indirect=True)
def test_undo_move(display_widget, qtbot):
    """
    Test that undoing a move updates the board correctly.
    """
    # Simulate a few moves
    display_widget.board.push_san("e4")
    display_widget.board.push_san("e5")
    # Undo last move
    display_widget.undoMove()
    assert display_widget.board.fen().startswith("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"), "Undo should revert to the state before the last move."


@pytest.mark.parametrize('display_widget', [(['', ''])], indirect=True)
def test_redo_move(display_widget, qtbot):
    """
    Test that redoing a move updates the board correctly after an undo.
    """
    # Simulate a move and undo it
    display_widget.board.push_san("e4")
    initial_fen = display_widget.board.fen()
    display_widget.undoMove()
    # Redo the move
    display_widget.redoMove()
    assert display_widget.board.fen() == initial_fen, "Redo should restore the board to the state before the undo."


@pytest.mark.parametrize('display_widget', [(['', ''])], indirect=True)
def test_checkmate_display(display_widget, qtbot):
    """
    Test that the game outcome label updates to show checkmate correctly.
    """
    # Set up a checkmate position manually
    display_widget.board.set_fen("7k/5QPP/8/8/8/8/8/7K w - - 0 1")
    display_widget.board.push_san("g8=Q#")
    display_widget.drawBoard()
    assert "Checkmate" in display_widget.turnLabel.text(), "Game outcome label should indicate checkmate."


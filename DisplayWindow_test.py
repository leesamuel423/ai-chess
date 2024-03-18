import pytest
from unittest.mock import patch
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtTest import QTest
from DisplayWindow import DisplayWindow

@pytest.fixture
def display_widget(request):
    """
    Fixture to create and return a Display widget with a patched 'input' value.
    The request.param will dictate the behavior for 'input' return values.
    """
    input_values = request.param
    with patch('builtins.input', side_effect=input_values):
        widget = DisplayWindow()
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

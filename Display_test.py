import pytest

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtTest import QTest

from Display import *


@pytest.fixture
def display_widget():
    """
    Fixture to create and return a Display widget.
    """
    widget = Display()
    widget.show()  # Necessary to test certain UI interactions
    return widget

def test_close_shortcut(display_widget, qtbot):
    """
    Test that the Display widget closes when the Ctrl+W shortcut is used.
    """
    # The widget should initially be visible
    assert display_widget.isVisible() == True

    # Simulate pressing Ctrl+W
    QTest.keyPress(display_widget, Qt.Key.Key_W, Qt.KeyboardModifier.ControlModifier)

    # Process events to ensure the UI responds to the shortcut
    QApplication.processEvents()

    # Verify the widget is no longer visible, indicating it has been closed
    assert display_widget.isVisible() == False

def test_minimize_shortcut(display_widget, qtbot):
    """
    Test that the Display widget minimizes when the Ctrl+M shortcut is used.
    """
    assert display_widget.isVisible() == True
    QTest.keyPress(display_widget, Qt.Key.Key_M, Qt.KeyboardModifier.ControlModifier)

    # Process events to ensure the UI responds to the shortcut
    QApplication.processEvents()

    # Verify the widget is minimized
    assert display_widget.isMinimized() == True

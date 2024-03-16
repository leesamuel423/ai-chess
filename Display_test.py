import pytest
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtTest import QTest

from Display import *


# Initialize a single QApplication instance for all tests
@pytest.fixture(scope='session')
def qapplication():
    return QApplication(sys.argv)

@pytest.fixture
def display_widget():
    """Fixture to create and return a Display widget."""
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

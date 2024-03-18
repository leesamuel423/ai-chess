import sys
from DisplayWindow import *
from PyQt6.QtWidgets import QApplication


def main():
    app = QApplication([]) # initialize QApplication (required for PyQt apps)
    window = DisplayWindow() # create DisplayWindow instance
    window.show()
    app.processEvents() # process any pending events for app
    sys.exit(app.exec()) # execute app and exit window when user closes window


if __name__ == "__main__":
    main()

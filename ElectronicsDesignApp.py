#!/usr/bin/env python3
'''
=====================
ECE 2524 - Project 3
=====================
Before running, go to the terminal and enter:
    pip3 install PySide2 --user
to get the latest version of Qt for Python only for current (user)

or:
    python3 -m venv ./<DIR>
    source <DIR>/bin/activate
    cd <DIR>
    pip3 install PySide2
to put the latest version of Qt for Python in a new virtual environment directory

Then, test the Installation in Python3 shell:
    import PySide2.QtCore
    print(PySide2.__version__)
    print(PySide2.__version_info__)
    print(PySide2.QtCore.__version__)
    print(PySide2.QtCore.__version_info__)
'''

import sys
import math
#import PySide2.QtCore
from PySide2 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.testText = ["foo", "bar"]
        self.testState = 0
        
        self.button = QtWidgets.QPushButton("Click to Toggle")
        self.text = QtWidgets.QLabel("Hello World!")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.toggle)

    def toggle(self):
        if self.testState == 0:
            self.text.setText(self.testText[0])
            self.testState = 1
        else:
            self.text.setText(self.testText[1])
            self.testState = 0


def main():
    print('\n' + 'begin test' + '\n')
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
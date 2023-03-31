'''
@author: Hanz Aquino
A UI for my Math expression solver algorithm called MathExParser
'''

__author__ = 'Hanz Aquino'
__version__ = '$Revision: 1.0 $'
__datecreated__ = '$Date: 2022-02-17 $'

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.main import MainUI
import sys
import os

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create main window object
    window = QMainWindow()
    window.setWindowIcon(
        QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'resources\\favicon.ico'))

    # create main ui object
    ui = MainUI(window)

    window.show()

    sys.exit(app.exec())

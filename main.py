from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget

from ui.MainWindow_ui import Ui_MainWindow
from ui.main_ui import main_ui
import sys


app = QApplication(sys.argv)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = main_ui()

    main_window.set_example("kjh")
    main_window.show()
    sys.exit(app.exec())

if __name__=='__main__':
    main()

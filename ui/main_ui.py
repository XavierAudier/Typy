from PyQt6 import QtWidgets, QtGui, QtCore
from ui.MainWindow_ui import Ui_MainWindow

class main_ui(QtWidgets.QMainWindow):

    # def __init__(self, parent = None, flags = None):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.text_input.textChanged.connect(self.refresh_example)
        f = self.ui.text_example.font()
        f.setPointSizeF(32.0)
        self.ui.text_example.setFont(f)
        self.ui.text_input.setFont(f)
        self.ui.text_input.setFocus()

    def set_example(self, new_example):
        self.ui.text_example.setText(new_example)
 
    def refresh_example(self):
        input = self.ui.text_input.text()
        example =  self.ui.text_example.text()
 
        if input == example:
            exit()
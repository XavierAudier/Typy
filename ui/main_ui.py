from PyQt5 import QtWidgets, QtGui, QtCore

class main_ui(QtWidgets.QMainWindow):

    # def __init__(self, parent = None, flags = None):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setGeometry(500, 500, 500, 100)


        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        # self.main_layout = QtWidgets.QVBoxLayout()
        # self.text_example_box = QtWidgets.QFrame()
        self.text_example = QtWidgets.QTextEdit()
        # self.text_example_box.setLayout(QtWidgets.QBoxLayout())
        # self.text_example_box.layout().addWidget(self.text_example)

        self.text_example.setEnabled(False)
        # self.text_example.setTextBackgroundColor(QtGui.QColor('red'))
        self.main_layout.addWidget(self.text_example, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.main_layout.setAlignment(self.text_example, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.text_example.setFontPointSize(16.0)
        self.text_example.setFontWeight(2)
        self.text_example.setTextColor(QtGui.QColor('black'))

        self.text_example.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.text_input = QtWidgets.QTextEdit()
        self.main_layout.addWidget(self.text_input)
        self.text_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.text_input.textChanged.connect(self.refresh_example)
        
        # self.setLayout(main_layout)
    def set_example(self, new_example):
        self.text_example.setText(new_example)

    def refresh_example(self):
        input = self.text_input.toPlainText()
        example =  self.text_example.toPlainText()
 
        if input == example:
            exit()
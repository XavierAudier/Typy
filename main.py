from PyQt5.QtWidgets import QApplication, QWidget
from ui.main_ui import main_ui
import sys


app = QApplication(sys.argv)


def main():
    main_window = main_ui()
    # main_window.setup_ui()
    main_window.set_example("kjh")
    
    main_window.show()
    # Start the event loop.
    app.exec()


if __name__=='__main__':
    main()

import sys
from PyQt5 import QtWidgets
from gui.main import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow('./gui/main.ui')
    sys.exit(app.exec())
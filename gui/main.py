# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import uic, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = uic.loadUi('./main.ui', self)
        self.window.show()

    def prevImage(self):
        pass

    def nextImage(self):
        pass

    def toggleMode(self):
        pass

    def readFolders(self):
        print(self.edPath.toPlainText())

    def changeFolder(self, index: int):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
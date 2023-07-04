import copy
import sys
from collections import deque
from api.io import FolderLoader
from PyQt5 import uic, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = uic.loadUi('./main.ui', self)
        self.window.show()
        self.previews = deque([self.lb1, self.lb2, self.lb3, self.lb4, self.lb5])
        self.__batch = None
        self.__pivot = 0

    def prevImage(self):
        pass

    def nextImage(self):
        pass

    def toggleMode(self):
        pass

    def readFolders(self):
        folders = FolderLoader.load_path(self.edPath.toPlainText())
        self.cbFolders.clear()
        for folder in folders:
            self.cbFolders.addItem(folder)

    def updateImages(self):
        files = FolderLoader.get_txts()
        if len(files) == 1:
            self.__pivot = 0
            self.__batch = FolderLoader.get_contents(files[0])
            sub_batch = self.__make_sub_batch()


    def changeFolder(self, index: int):
        pass

    def __make_sub_batch(self):
        sub_batch = []
        for index in range(self.__pivot - 2, self.__pivot + 3):
            if index < 0 or len(self.__batch) >= index:
                stub = None
            else:
                stub = copy.deepcopy(self.__batch[index])
            sub_batch.append(stub)
        return sub_batch

    def __update_previews(self, sub_batch):
        for stub in sub_batch:
            if stub is None:
                continue


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
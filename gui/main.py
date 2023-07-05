import copy
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QKeyEvent, QImage
from api.io import FolderLoader
from api.draw import draw_points
from PyQt5 import uic, QtWidgets
import qimage2ndarray


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, path, parent=None):
        super().__init__(parent)
        self.window = uic.loadUi(path, self)
        self.window.show()
        self.previews = [self.lb1, self.lb2, self.lb3, self.lb4, self.lb5]
        size = self.previews[0].size()
        self.preview_size = (size.width(), size.height())

        size = self.lbMain.size()
        self.display_size = (size.width(), size.height())

        self.__batch = None
        self.__pivot = 0
        self.edPath.setPlainText(r'D:\Creadto\Heritage\Dataset\Facial landmarks')
        self.readFolders()
        self.updateImages()

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == Qt.Key_Comma:
            self.prevImage()
        elif a0.key() == Qt.Key_Period:
            self.nextImage()
        else:
            pass

    def prevImage(self):
        if self.__pivot > 0:
            self.__pivot -= 1

        self.__update_previews()

    def nextImage(self):
        if self.__pivot < len(self.__batch) - 1:
            self.__pivot += 1

        self.__update_previews()

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
            self.__update_previews()

    def changeFolder(self, index: int):
        current_index = self.cbFolders.currentIndex()
        FolderLoader.change_index(current_index)
        self.updateImages()


    def __make_sub_batch(self):
        sub_batch = []
        for index in range(self.__pivot - 2, self.__pivot + 3):
            if index < 0 or len(self.__batch) <= index:
                stub = None
            else:
                stub = copy.deepcopy(self.__batch[index])
            sub_batch.append(stub)
        return sub_batch

    def __update_previews(self):
        sub_batch = self.__make_sub_batch()
        for number, stub in enumerate(sub_batch):
            if stub is None:
                image_path = r'./bk.jpg'
                pixmap = QPixmap(image_path)
            else:
                image = FolderLoader.load_image(stub['filename'])
                draw_image = draw_points(image, stub['coordinates'])
                resized = cv2.resize(draw_image, self.preview_size)
                q_image = qimage2ndarray.array2qimage(resized, normalize=False)
                pixmap = QPixmap.fromImage(q_image)

            self.previews[number].setPixmap(pixmap)
        self.display()

    def display(self):
        image = FolderLoader.load_image(self.__batch[self.__pivot]['filename'])
        draw_image = draw_points(image, self.__batch[self.__pivot]['coordinates'])
        resized = cv2.resize(draw_image, self.display_size)
        q_image = qimage2ndarray.array2qimage(resized, normalize=False)
        pixmap = QPixmap.fromImage(q_image)
        self.lbMain.setPixmap(pixmap)

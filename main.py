import cv2
import numpy as np
import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class DisplayImageWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DisplayImageWidget, self).__init__(parent)

        self.restart = QtWidgets.QPushButton("Show picture")
        self.restart.clicked.connect(self.show_image)
        self.image_frame = QtWidgets.QLabel()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.restart)
        self.layout.addWidget(self.image_frame)
        self.setLayout(self.layout)


    def stop_draw(self):
        stop_value = 1


    #@QtCore.pyqtSlot()
    def show_image(self):

        image = cv2.imread("test2.png")
        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        thresh = cv2.adaptiveThreshold(
            image_gray,
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            21,
            15,
        )

        # thresh = (255-thresh)
        # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
        contours, hierarchy = cv2.findContours(
            image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE
        )

        image_created = np.full((image.shape), 255, dtype=np.uint8)
        contours.sort(key=len)
        contours.reverse()

        self.image = image_created
        self.image = QtGui.QImage(
            self.image.data,
            self.image.shape[1],
            self.image.shape[0],
            QtGui.QImage.Format_RGB888,
        ).rgbSwapped()

        for list in contours:
            list.resize(list.shape[0], list.shape[2])

            for tuple in list:
                cv2.line(image_created, tuple, tuple + 1, (0, 0, 0), 1)
                self.image = image_created
                self.image = QtGui.QImage(
                    self.image.data,
                    self.image.shape[1],
                    self.image.shape[0],
                    QtGui.QImage.Format_RGB888,
                ).rgbSwapped()
                self.image_frame.setPixmap(QtGui.QPixmap.fromImage(self.image))
                cv2.waitKey(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    display_image_widget = DisplayImageWidget()
    display_image_widget.show()
    sys.exit(app.exec_())

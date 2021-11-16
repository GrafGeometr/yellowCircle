import sys
from random import randrange as r

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPoint


class CircleMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        # self.doButton.clicked.connect(self.do)
        self.x, self.y = self.size().width(), self.size().height()
        self.doButton.clicked.connect(self.mark)
        self.paint = False
        # print(self.x,self.y)
        # qp.end()

    def mark(self):
        self.paint = True
        self.update()

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.do(qp)
            qp.end()
            self.paint = False

    def do(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x, y = r(self.x), r(self.y)
        rx, ry = r(min(x, self.x - x)) - 1, r(min(y, self.y - y)) - 1
        R = min(rx, ry)
        # print(x, y, R, R)
        qp.drawEllipse(QPoint(x, y), R, R)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleMaker()
    ex.show()
    sys.exit(app.exec())

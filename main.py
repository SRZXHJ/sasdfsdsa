import random
import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.btn = QPushButton('Рисовать', self)

    def initUI(self):
        self.setGeometry(500, 300, 500, 500)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(210, 400)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()


    def paint(self):
        self.do_paint = True
        self.repaint()


    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        s = random.randrange(15, 250)
        y = random.randrange(5, 300)
        x = random.randrange(5, 300)
        qp.drawEllipse(x, y, s, s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
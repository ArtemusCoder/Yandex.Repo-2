import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git и желтые окружности')
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QColor(255, 255, 0))
        x = random.randint(0, 750)
        y = random.randint(0, 380)
        diameter = random.randint(10, 50)
        qp.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("number1.ui", self)

        self.pushButton.clicked.connect(self.computeFahrenheit)
        self.pushButton_2.clicked.connect(self.computeCelsius)
        self.show()

    def computeFahrenheit(self):
        thing = self.celsius.text()
        op = str(9.0 / 5.0 * int(thing) + 32)
        self.fahrenheit.setText(op)

    def computeCelsius(self):
        thing = self.fahrenheit.text()
        op = str((int(thing) - 32) * 5.0 / 9.0)
        self.celsius.setText(op)


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
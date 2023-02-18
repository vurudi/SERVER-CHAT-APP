from PyQt5.QtWidgets import *
from PyQt5 import uic
class MyGui(QMainWindow):
    def __init__(self):
        super(MyGui, self).__init__()

        uic.loadUi("SERVER UI.ui", self)
        self.show()


    def main(self):
        app = QApplication([])
        window = MyGui()
        app.exec_()


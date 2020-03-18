from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

class Window(QMainWindow):
    def __init__(self,):
        QMainWindow.__init__(self)

        self.show()

app=QApplication(sys.argv)
window=Window()
sys.exit(app.exec())
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QVBoxLayout,QDialog
import sys

class Window(QDialog):
    def __init__(self,):
        QDialog.__init__(self)
        self.setMinimumSize(500,400)
        vbox=QVBoxLayout()
        button=QPushButton("Click Me")
        button.clicked.connect(self.click)
        vbox.addWidget(button)
        self.setLayout(vbox)
        
        self.show()
    def click(self):
        print("clicked")
    

app=QApplication(sys.argv)
window=Window()
sys.exit(app.exec())
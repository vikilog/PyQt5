from PyQt5 import QtWidgets,QtGui,QtCore
import sys

class MainGUi(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setWindowIcon(QtGui.QIcon("icon.jpg"))
        self.setWindowTitle("Pizza Wings")
        

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    w=MainGUi()
    w.show()
    sys.exit(app.exec())
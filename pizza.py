from PyQt5 import QtWidgets, QtCore, Qt, QtGui
import sys


class PizzaApp(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setWindowTitle("Pizza Wings")
        self.setFixedSize(800,500)
        self.initUI()

    def initUI(self):
        label = QtWidgets.QLabel(self)
        self.setStyleSheet("background-image:url(pizza.jpg);background-attachment: fixed;   background-position: center;")
        self.setWindowIcon(QtGui.QIcon("icon.jpg"))
        titlelabel = QtWidgets.QLabel(self)
        titlelabel.setText("Pizza Wings")
        titlelabel.move(200, 50)
        titlelabel.setStyleSheet("color:white;font-size:50px;background:transparent")
        themelabel = QtWidgets.QLabel(self)
        themelabel.setText("Welcome to Pizza Wings")
        themelabel.setStyleSheet("color:white;font-size:30px;background:transparent")
        themelabel.move(200, 120)
        emaillabel = QtWidgets.QLabel(self)
        emaillabel.setText("Email")
        emaillabel.move(100, 200)
        emaillabel.setStyleSheet("color:white;font-size:30px;background:transparent")
        emailinput=QtWidgets.QLineEdit(self)
        emailinput.move(250,200)
        emailinput.setStyleSheet("font-size:30px;color:white;background:transparent")
        passwordlabel = QtWidgets.QLabel(self)
        passwordlabel.setText("Password")
        passwordlabel.move(100, 250)
        passwordlabel.setStyleSheet("color:white;font-size:30px;background:transparent")
        passwordinput=QtWidgets.QLineEdit(self)
        passwordinput.move(250,250)
        passwordinput.setStyleSheet("font-size:30px;color:white;background:transparent")
        loginbutton=QtWidgets.QPushButton(self)
        loginbutton.setText("Log In")
        loginbutton.setToolTip("Click to log in")
        loginbutton.setGeometry(300,320,200,50)
        loginbutton.setStyleSheet("border:0.1em solid #FFFFFF;border-radius:10px;font-family:'Roboto',sans-serif;font-weight:300;color:White;text-align:center;font-size:20px")
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pizza = PizzaApp()
    pizza.show()
    sys.exit(app.exec())

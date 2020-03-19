from PyQt5 import QtWidgets, QtCore, Qt, QtGui
import sys
import sqlite3
from mainwindow import MainGUi


class PizzaApp(QtWidgets.QDialog):
    def openWindow(self):        
        self.window=QtWidgets.QMainWindow()
        self.w=MainGUi()
        PizzaApp.hide(self)
        self.w.showMaximized()   

    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)

        def login():
            email=emailinput.text()
            password=passwordinput.text()            
            mydb=sqlite3.connect("pizzawing.db")
            mycursor=mydb.cursor()
            mycursor.execute(f"SELECT * FROM user")
            userinfo=mycursor.fetchall()          
            for e,p in userinfo:
                if email =="" and password =="":               
                    infolabel.setText("Email and Password can'nt empty")
                    infolabel.setStyleSheet("font-size:20px;color:red")
                else:
                    if e==email and password==p:
                        infolabel.setText("Log in Sucessfully")
                        infolabel.setStyleSheet("font-size:20px;color:green")
                        self.openWindow()                       
                    else:
                        if e!=email:
                            infolabel.setText("Please enter a valid email")
                            infolabel.setStyleSheet("font-size:20px;color:red")
                        elif p !=password:
                            infolabel.setText("Please enter correct password")
                            infolabel.setStyleSheet("font-size:20px;color:red")
                        else:
                            infolabel.setText("Please enter valid email and password")
                            infolabel.setStyleSheet("font-size:20px;color:red")         
                  
        self.setWindowTitle("Pizza Wings")
        self.setFixedSize(800,500)      
        label = QtWidgets.QLabel(self)
        self.setStyleSheet("background-image:url(bg.png);background-attachment: fixed;   background-position: center;")
        self.setWindowIcon(QtGui.QIcon("icon.jpg"))
        titlelabel = QtWidgets.QLabel(self)
        titlelabel.setText("Pizza Wings")
        titlelabel.move(230, 30)
        titlelabel.setStyleSheet("color:white;font-size:70px;background:transparent;")
        themelabel = QtWidgets.QLabel(self)
        themelabel.setText("Welcome to Pizza Wings")
        themelabel.setStyleSheet("color:white;font-size:40px;background:transparent;")
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
        passwordinput.setEchoMode(QtWidgets.QLineEdit.Password)
        passwordinput.move(250,250)
        passwordinput.setStyleSheet("font-size:30px;color:white;background:transparent")
        loginbutton=QtWidgets.QPushButton(self)
        loginbutton.setText("Log In")
        loginbutton.setToolTip("Click to log in")
        loginbutton.setGeometry(300,320,200,50)
        loginbutton.setStyleSheet("border:0.1em solid #FFFFFF;border-radius:10px;font-family:'Roboto',sans-serif;font-weight:300;color:White;text-align:center;font-size:20px")
        loginbutton.clicked.connect(lambda:login())
        infolabel=QtWidgets.QLabel(self)
         
        infolabel.setText("Please enter details to log in")
        infolabel.setStyleSheet("font-size:20px;color:white")
        infolabel.setGeometry(250,400,400,100)      

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pizza = PizzaApp()
    pizza.show()    
    sys.exit(app.exec())

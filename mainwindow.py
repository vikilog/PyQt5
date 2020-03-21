from PyQt5 import QtWidgets,QtGui,QtCore
import sys



class MainGUi(QtWidgets.QMainWindow):
    
    def logOut(self):
        import pizza
        self.p=pizza.PizzaApp()
        self.p.show()
        MainGUi.hide(self)           
            
    

    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        pizzasize=""
        topping=""
        pizzaFlavour=""
        crust=""
        self.setWindowIcon(QtGui.QIcon("icon.jpg"))
        self.setWindowTitle("Pizza Wings")
        self.initUI()
        # self.setStyleSheet("background-image:url(mainbg.jpg);background-attachment: fixed;   background-position: center;")
    

    def initUI(self):
        titlelabel=QtWidgets.QLabel(self)
        titlelabel.setText("Welcome to Pizza wing")
        titlelabel.setGeometry(300,5,800,150)        
        titlelabel.setStyleSheet("font-size:70px;background:transparent;")
        sizelabel=QtWidgets.QLabel(self)
        sizelabel.setText("Size : ")
        sizelabel.setGeometry(90,165,100,100)
        sizelabel.setStyleSheet("font-size:30px")
        sizeFrame=QtWidgets.QFrame(self)
        sizeFrame.setStyleSheet("color:red")
        sizeFrame.setGeometry(50,170,500,100)
        sizeFrame.setLineWidth(0.6)
        sizeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        smallradiobtn=QtWidgets.QRadioButton(self)        
        smallradiobtn.setText("Small")
        smallradiobtn.move(200,200,)
        smallradiobtn.setStyleSheet("font-size:20px")
        mediumradiobtn=QtWidgets.QRadioButton(self)
        mediumradiobtn.setText("Medium")
        mediumradiobtn.move(320,200,)
        mediumradiobtn.setStyleSheet("font-size:20px")
        largeradiobtn=QtWidgets.QRadioButton(self)
        largeradiobtn.setText("Large")
        largeradiobtn.move(450,200,)
        largeradiobtn.setStyleSheet("font-size:20px")        
        smallradiobtn.toggled.connect(lambda :getPizzaSize())
        mediumradiobtn.toggled.connect(lambda :getPizzaSize())
        largeradiobtn.toggled.connect(lambda :getPizzaSize())

        pizzatypeFrame=QtWidgets.QFrame(self)
        pizzatypeFrame.setStyleSheet("color:red")
        pizzatypeFrame.setGeometry(50,300,500,100)
        pizzatypeFrame.setLineWidth(0.6)
        pizzatypeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        pizzatypelabel=QtWidgets.QLabel(self)
        pizzatypelabel.setText("Crust :")
        pizzatypelabel.move(90,325)
        pizzatypelabel.setStyleSheet("font-size:30px")
        thincrustradiobtn=QtWidgets.QRadioButton(self)
        thincrustradiobtn.setText("Thin")
        thincrustradiobtn.move(200,325,)
        thincrustradiobtn.setStyleSheet("font-size:20px")
        mediumcrustradiobtn=QtWidgets.QRadioButton(self)
        mediumcrustradiobtn.setText("Medium")
        mediumcrustradiobtn.move(320,325,)
        mediumcrustradiobtn.setStyleSheet("font-size:20px")
        pancrustradiobtn=QtWidgets.QRadioButton(self)
        pancrustradiobtn.setText("Pan")
        pancrustradiobtn.move(450,325,)
        pancrustradiobtn.setStyleSheet("font-size:20px")
        thincrustradiobtn.toggled.connect(lambda :getCrust())
        mediumcrustradiobtn.toggled.connect(lambda :getCrust())
        pancrustradiobtn.toggled.connect(lambda :getCrust())

        flavorFrame=QtWidgets.QFrame(self)
        flavorFrame.setStyleSheet("color:red")
        flavorFrame.setGeometry(50,420,250,250)
        flavorFrame.setLineWidth(0.6)
        flavorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        flavorlabel=QtWidgets.QLabel(self)
        flavorlabel.setText("Select Flavour")
        flavorlabel.setStyleSheet("font-size:30px")
        flavorlabel.setGeometry(90,420,250,50)
        tomatocheckbox=QtWidgets.QCheckBox(self)
        tomatocheckbox.setText("Tomato")
        tomatocheckbox.setStyleSheet("font-size:20px")
        tomatocheckbox.move(80,480)
        corncheckbox=QtWidgets.QCheckBox(self)
        corncheckbox.setText("Corn")
        corncheckbox.setStyleSheet("font-size:20px")
        corncheckbox.move(80,530)
        onioncheckbox=QtWidgets.QCheckBox(self)
        onioncheckbox.setText("Onion")
        onioncheckbox.setStyleSheet("font-size:20px")
        onioncheckbox.move(80,580)
        capsicumcheckbox=QtWidgets.QCheckBox(self)
        capsicumcheckbox.setText("Capsicum")
        capsicumcheckbox.setStyleSheet("font-size:20px")
        capsicumcheckbox.move(80,630)

        toppingFrame=QtWidgets.QFrame(self)      
        toppingFrame.setStyleSheet("color:red")
        toppingFrame.setGeometry(310,420,240,250)
        toppingFrame.setLineWidth(0.6)
        toppingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        toppinglabel=QtWidgets.QLabel(self)
        toppinglabel.setText("Topping")
        toppinglabel.move(350,430)
        toppinglabel.setStyleSheet("font-size:25px")
        mushroomTopping=QtWidgets.QCheckBox(self)
        mushroomTopping.setText("Mushrooms")
        mushroomTopping.move(330,470)
        mushroomTopping.setStyleSheet("font-size:20px")
        cheeseTopping=QtWidgets.QCheckBox(self)
        cheeseTopping.setText("Cheese")
        cheeseTopping.move(330,500)
        cheeseTopping.setStyleSheet("font-size:20px")
        peproniTopping=QtWidgets.QCheckBox(self)
        peproniTopping.setText("Peproni")
        peproniTopping.move(330,530)
        peproniTopping.setStyleSheet("font-size:20px")
        sausageTopping=QtWidgets.QCheckBox(self)
        sausageTopping.setText("Sausage")
        sausageTopping.move(330,560)
        sausageTopping.setStyleSheet("font-size:20px")

        orderText=QtWidgets.QPlainTextEdit(self)
        orderText.insertPlainText("\t\tPizza Wing")
        orderText.move(560,170)
        orderText.resize(500,500)
        orderText.setReadOnly(True)
        orderText.setStyleSheet("font-size:30px")

        logoutbtn=QtWidgets.QPushButton(self)
        logoutbtn.setText("Log Out")
        logoutbtn.setGeometry(1100,200,200,50)
        logoutbtn.clicked.connect(lambda:self.logOut())

        resetButton=QtWidgets.QPushButton(self)
        resetButton.setText("Reset")      
        resetButton.setGeometry(1100,300,200,50)
        resetButton.clicked.connect(lambda :reset())
        
        printButton=QtWidgets.QPushButton(self)
        printButton.setText("Place Order")      
        printButton.setGeometry(1100,400,200,50)
        printButton.clicked.connect(lambda :getPizzaSize())
        
        exitButton=QtWidgets.QPushButton(self)
        exitButton.setText("Exit")      
        exitButton.setGeometry(1100,500,200,50)
        exitButton.clicked.connect(lambda :exit())

        def reset():
            orderText.setReadOnly(False)
            orderText.clear()
            orderText.setReadOnly(True)

        def exit():
            MainGUi.close(self)
        
        def getPizzaSize():
            if  smallradiobtn.isChecked():
                orderText.insertPlainText("\nPizza Size : Small")
            elif mediumradiobtn.isChecked():
                orderText.insertPlainText("\nPizza Size : Medium")
            elif largeradiobtn.isChecked():
                orderText.insertPlainText("\nPizza Size : Large")
           
        def getCrust():
            if thincrustradiobtn.isChecked():
                orderText.insertPlainText("\nCrust Type : Thin")
            elif mediumcrustradiobtn.isChecked():
                orderText.insertPlainText("\nCrust Type : Medium")
            elif pancrustradiobtn.isChecked():
                orderText.insertPlainText("\nCrust Type : Pan")

                
                
            

        

        

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    w=MainGUi()
    w.showMaximized()
    sys.exit(app.exec())
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, random, time 

class Window(QMainWindow):
    def __init__(self):
        self.MasterPass="12345"
        self.item=None
        super(Window,self).__init__()
        self.setStyleSheet("background-color: #0ABAA9;")
        self.setGeometry(600,350,600,300)
        self.setWindowTitle("PassManager")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setMaximumSize(600,300)
        self.setMinimumSize(600,300)
        self.initUI()
        
        
    def addItem(self,text):
        item=QListWidgetItem(text)
        self.list.addItem(item)
        widget=QtWidgets.QWidget(self.list)
        button=QtWidgets.QPushButton(widget)
        button.setText("X")
        
        button.clicked.connect(lambda: self.removeItem(item))
        layout = QtWidgets.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button)
        self.list.setItemWidget(item,widget)

    def removeItem(self,item):
        print(item.text())
        text=item.text()
        self.list.takeItem(self.list.row(item))
        file=open("db.txt","r")
        list=file.readlines()
        file=open("db.txt","w")
        for l in list:
            if l.strip("\n")!=text:
                file.write(l.strip("\n"))
                file.write("\n")
        file.close()
    def initUI(self):
        self.label1=QtWidgets.QLabel(self)
        self.label1.setGeometry(175,20,250,25)
        self.label1.setText("Enter the master password")
        self.label1.setFont(QFont('Arial',12))
        self.label1.setStyleSheet("border: 1px solid black;")
        ##########
        self.text1=QtWidgets.QLineEdit(self)
        self.text1.setGeometry(220,55,160,35)
        self.text1.setFont(QFont('Arial',12))
        self.text1.setStyleSheet("border: 1px solid black;")
        self.text1.setEchoMode(QtWidgets.QLineEdit.Password)
        ##########
        self.button1=QtWidgets.QPushButton(self)
        self.button1.setGeometry(260,100,80,30)
        self.button1.setFont(QFont('Arial',10))
        self.button1.setStyleSheet('QPushButton {background-color: #0ABA66; color: black; border: 1px solid black;}')
        self.button1.setText("Access")
        self.button1.clicked.connect(self.Access)
        ##########
        self.label2=QtWidgets.QLabel(self)
        self.label2.setGeometry(60,45,47,25)
        self.label2.setText("Site")
        self.label2.setFont(QFont('Arial',12))
        self.label2.setStyleSheet("border: 1px solid black;")
        self.label2.setVisible(False)
        ##########
        self.label3=QtWidgets.QLabel(self)
        self.label3.setGeometry(46,85,60,25)
        self.label3.setText("Email")
        self.label3.setFont(QFont('Arial',12))
        self.label3.setStyleSheet("border: 1px solid black;")
        self.label3.setVisible(False)
        ##########
        self.label4=QtWidgets.QLabel(self)
        self.label4.setGeometry(11,125,96,25)
        self.label4.setText("Password")
        self.label4.setFont(QFont('Arial',12))
        self.label4.setStyleSheet("border: 1px solid black;")
        self.label4.setVisible(False)
        ##########
        self.label5=QtWidgets.QLabel(self)
        self.label5.setGeometry(200,10,200,25)
        self.label5.setText("Add a new password")
        self.label5.setFont(QFont('Arial',12))
        self.label5.setStyleSheet("border: 1px solid black;")
        self.label5.setVisible(False)
        ##########
        self.text2=QtWidgets.QLineEdit(self)
        self.text2.setGeometry(110,40,420,35)
        self.text2.setFont(QFont('Arial',12))
        self.text2.setStyleSheet("border: 1px solid black;")
        self.text2.setVisible(False)
        ##########
        self.text3=QtWidgets.QLineEdit(self)
        self.text3.setGeometry(110,80,420,35)
        self.text3.setFont(QFont('Arial',12))
        self.text3.setStyleSheet("border: 1px solid black;")
        self.text3.setVisible(False)
        ##########
        self.text4=QtWidgets.QLineEdit(self)
        self.text4.setGeometry(110,120,420,35)
        self.text4.setFont(QFont('Arial',12))
        self.text4.setStyleSheet("border: 1px solid black;")
        self.text4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text4.setVisible(False)
        #########
        self.button2=QtWidgets.QPushButton(self)
        self.button2.setGeometry(220,200,180,30)
        self.button2.setFont(QFont('Arial',10))
        self.button2.setStyleSheet('QPushButton {background-color: #0ABA66; color: black; border: 1px solid black;}')
        self.button2.setText("See passwords")
        self.button2.setVisible(False)
        self.button2.clicked.connect(self.PassManager)
        #########
        self.button3=QtWidgets.QPushButton(self)
        self.button3.setGeometry(220,160,180,30)
        self.button3.setFont(QFont('Arial',10))
        self.button3.setStyleSheet('QPushButton {background-color: #0ABA66; color: black; border: 1px solid black;}')
        self.button3.setText("Add new password")
        self.button3.setVisible(False)
        self.button3.clicked.connect(self.Add)
        ########
        self.list = QListWidget()
        self.list.setWindowTitle("PassManager")
        self.list.setGeometry(500,400,850,350)
        self.list.setMinimumSize(850,350)
        self.list.setMaximumSize(1225,500)
        self.list.setVisible(False)
        self.list.setWindowIcon(QtGui.QIcon('icon.png'))
    def Access(self):
        password=self.text1.text()
        if password==self.MasterPass:
            self.button1.setVisible(False)
            self.text1.setVisible(False)
            self.label1.setVisible(False)
            self.label2.setVisible(True)
            self.label3.setVisible(True)
            self.label4.setVisible(True)
            self.label5.setVisible(True)
            self.text2.setVisible(True)
            self.text3.setVisible(True)
            self.text4.setVisible(True)
            self.button2.setVisible(True)
            self.button3.setVisible(True)
        else:
            QMessageBox.about(self, "PassManager", "Wrong password, try again!")
            self.text1.clear()
    def PassManager(self):
        self.list.setVisible(True)
    def encoder(self,text):
        s=""
        for l in text:
            s+=str(ord(l)+30)+"."
        return s 
    def decoder(self,text):
        text=text.split(".")
        text=text[:len(text)-1]
        s=""
        for c in text:
            s+=chr(int(c)-30)
        return s    
    def Add(self):
        site=self.text2.text()
        email=self.text3.text()
        password=self.text4.text()
        password=self.encoder(password)
        if len(email)==0 or len(site)==0 or len(password)==0:
            QMessageBox.about(self, "PassManager", "All fields must be completed!")
        else:
            self.text2.clear()
            self.text3.clear()
            self.text4.clear()
            file=open("db.txt","a")
            text="Site: {} Email: {} Password: {}".format(site,email,password)
            file.write(text)
            file.write("\n")
            file.close()
            self.addItem(self.modify(text))
    def modify(self,text):
        text=text.strip("\n")
        text=text.split(" ")
        password=text[len(text)-1]
        print(password)
        text[len(text)-1]="Password: {}".format(self.decoder(password))
        return " ".join(text)

def start():
    app=QApplication(sys.argv)
    window=Window()
    file=open("db.txt","r")
    list=file.readlines()
    for l in list:
        window.addItem(window.modify(l))
    window.show()
    sys.exit(app.exec_())

start()

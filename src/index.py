from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon,QApplication
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import os
from os import path
import sys
from main import Ui_MainWindow
import math
import random
import pyperclip

password = []
symboles = ['&','#','{','(','[','-','|','`','_','\'','^','@',',','.',';','?','>','<',':','/','!','§','*','µ','£','$','%','¨','°','}','+']
numbers = ["0","1","2","3","4",'5','6','7','8','9']
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
arSymboles = ['ّ','َ','ً','ِ','ٍ','ْ','ِ']

class MainApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Window()
        self.Handel_Buttons()
        self.Handel_CheckBoxes()

    def Handel_Window(self):
        self.setFixedSize(689, 297)
        self.setWindowTitle('Password generator')
        self.setWindowIcon(QtGui.QIcon('img/password.ico'))

    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.password_Generating)
        self.pushButton_2.clicked.connect(self.copy_Method)

    def Handel_CheckBoxes(self):
        self.checkBox.stateChanged.connect(self.numbers_Generating)
        self.checkBox_2.stateChanged.connect(self.letters_Generating)
        self.checkBox_3.stateChanged.connect(self.symboles_Generating)
        self.checkBox_4.stateChanged.connect(self.arSymboles_Generating)

    def symboles_Generating(self):
        symboles_Length = 32 * 20 / 100

        if symboles_Length != int(symboles_Length):
            symboles_Length = math.ceil(symboles_Length)

        for _ in range(0,int(symboles_Length)):
            password.append(symboles[random.randrange(0,len(symboles)-1)])

    def arSymboles_Generating(self):
        arSymboles_Length = 32 * 10 / 100

        if arSymboles_Length != int(arSymboles_Length):
            arSymboles_Length = math.ceil(arSymboles_Length)

        for _ in range(0, int(arSymboles_Length)):
            password.append(arSymboles[random.randrange(0, len(arSymboles) - 1)])

    def numbers_Generating(self):
        numbers_Length = 32 * 30 / 100

        if numbers_Length != int(numbers_Length):
            numbers_Length = math.ceil(numbers_Length)

        for _ in range(0,int(numbers_Length)):
            password.append(numbers[random.randrange(0,len(numbers)-1)])

    def letters_Generating(self):
        letters_Length = 32 * 40 / 100

        if letters_Length != int(letters_Length):
            letters_Length = math.ceil(letters_Length)

        for _ in range(0,int(letters_Length)):
            password.append(letters[random.randrange(0,len(letters)-1)])

    def password_Generating(self):
        password_Var = random.choices(password,k=32)
        password_Var2 = ''.join(password_Var)
        self.lineEdit.setText(password_Var2)

    def copy_Method(self):
        pyperclip.copy(self.lineEdit.text())
        paste = pyperclip.paste()









def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp() # نأخذ نسخة من الclass الي نقدر ننشأ منه window
    window.show() # لإظهار ال window
    app.exec_() # هذا عبارة عن loop يخلي ال window ظاهرة دائما في الشاشة، إذا لم تكن هذه ال loop رح تظهر ال window و تختفي على طول.


if __name__ == '__main__': # في هذا السطر إحنا بنحدد و نختار السطر الي رح يبدأ منه الكود و في هاذي الأسطر إخترنا أنه يبدأ من ال function 'main'
    main()
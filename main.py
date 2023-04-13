import sys
from tkinter import Widget
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

from RSA import *

import sqlite3
import os
import csv
import datetime
import random

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("main.ui", self)
        self.pushButton_5.clicked.connect(self.GenKey)
        self.pushButton_6.clicked.connect(self.DigitalSign)
        self.pushButton_7.clicked.connect(self.SignVerif)

    def DigitalSign(self):
        digitalSign = DigitalSign()
        widget.addWidget(digitalSign)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def GenKey(self):
        genKey = GenKey()
        widget.addWidget(genKey)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def SignVerif(self):
        signVerif = SignVerif()
        widget.addWidget(signVerif)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class GenKey(QMainWindow):
    def __init__(self):
        super(GenKey, self).__init__()
        loadUi("genkey.ui", self)
        self.pushButton_10.clicked.connect(self.Menu)
        self.pushButton_11.clicked.connect(self.PopUpGenerate)
    
    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def PopUpGenerate(self):
        namaFile = self.textEdit.toPlainText()
        if (namaFile == ""):
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("Nama File Masih Kosong Say :)")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("File Public dan Private Key Berhasil Tersimpan")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
        # Warning
        # Critical
        # Information
        # Question

class DigitalSign(QMainWindow):
    def __init__(self):
        super(DigitalSign, self).__init__()
        loadUi("digitalsign.ui", self)
        self.pushButton_10.clicked.connect(self.Menu)
        self.pushButton_11.clicked.connect(self.AddFile)
        self.pushButton_12.clicked.connect(self.AddPrivKeyFile)
        self.pushButton_13.clicked.connect(self.PopUpSign)
    
    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def AddFile(self):
        print("Ayo Clubbing")

    def AddPrivKeyFile(self):
        print("Ayo Clubbing")

    def PopUpSign(self):
        msg = QMessageBox()
        msg.setWindowTitle("Notification")
        msg.setText("Bla bla bla")
        msg.setIcon(QMessageBox.Critical)
        # Warning
        # Critical
        # Information
        # Question

        x = msg.exec_()

class SignVerif(QMainWindow):
    def __init__(self):
        super(SignVerif, self).__init__()
        loadUi("signverif.ui", self)
        self.pushButton_10.clicked.connect(self.Menu)
        self.pushButton_11.clicked.connect(self.AddFile)
        self.pushButton_12.clicked.connect(self.AddPubKeyFile)
        self.pushButton_13.clicked.connect(self.AddSignedFile)
        self.pushButton_14.clicked.connect(self.PopUpVerif)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def AddFile(self):
        print("Ayo Clubbing")

    def AddPubKeyFile(self):
        print("Ayo Clubbing")

    def AddSignedFile(self):
        print("Ayo Clubbing")

    def PopUpVerif(self):
        msg = QMessageBox()
        msg.setWindowTitle("Notification")
        msg.setText("Bla bla bla")
        msg.setIcon(QMessageBox.Critical)
        # Warning
        # Critical
        # Information
        # Question

        x = msg.exec_()

# main
app = QApplication(sys.argv)
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exit Program")
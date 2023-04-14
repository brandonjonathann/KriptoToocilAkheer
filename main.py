import sys
from tkinter import Widget
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

from RSA import *
from function import *
from SHA3 import *

import sqlite3
import os
import csv
import datetime
import random
import pathlib

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
            if (writeKey(namaFile)):
                msg = QMessageBox()
                msg.setWindowTitle("Notification")
                msg.setText("File Public dan Private Key Berhasil Tersimpan")
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Notification")
                msg.setText("Nama File Sudah Ada, Silahkan Masukan Nama File Lain ataupun Hapus File Sebelumnya")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()
        # Warning
        # Critical
        # Information
        # Question

class DigitalSign(QMainWindow):

    namefile = ''
    prifile = ''

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
        text = self.ReadFile()
        self.textBrowser.setPlainText(text)
        DigitalSign.namefile = text

    def AddPrivKeyFile(self):
        text = self.ReadPrivKeyFile()
        self.textBrowser_2.setPlainText(text)
        DigitalSign.prifile = text

    def ReadFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File")
        return (fname[0])
    
    def ReadPrivKeyFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File")
        if (pathlib.Path(fname[0]).suffix == ".pri"):
            return (fname[0])
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("Masukan File dengan Format .pri")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

    def PopUpSign(self):
        if (DigitalSign.namefile == '' or DigitalSign.prifile == ''):
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("Masukan File ataupun Private Key File yang Masih Kosong")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            with open("%s.pri" % (pathlib.Path(DigitalSign.prifile).stem), "rb") as rp:
                tmp = rp.read()
                key = str(tmp, 'utf-8').split(',')
                e = int(key[1])
                n = int(key[0])

            with open("%s.txt" % (pathlib.Path(DigitalSign.namefile).stem), "r+") as f:                
                tmp = (f.read())
                tmp = enkripsi(hash(tmp), e, n)

            with open('%s.txt' % (pathlib.Path(DigitalSign.namefile).stem), "a") as file:
                file.write("\n<ds>")
                file.write(tmp)
                file.write("</ds>")
                file.close()

            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("File Berhasil Di-sign")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        # Warning
        # Critical
        # Information
        # Question


class SignVerif(QMainWindow):

    namefile = ''
    pubfile = ''
    signfile = ''

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
        text = self.ReadFile()
        self.textBrowser.setPlainText(text)
        SignVerif.namefile = text

    def AddPubKeyFile(self):
        text = self.ReadPubKeyFile()
        self.textBrowser_2.setPlainText(text)
        SignVerif.pubfile = text

    def AddSignedFile(self):
        text = self.ReadSignKeyFile()
        self.textBrowser_3.setPlainText(text)
        SignVerif.signfile = text

    def ReadFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File")
        return (fname[0])
    
    def ReadPubKeyFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File")
        if (pathlib.Path(fname[0]).suffix == ".pub"):
            return (fname[0])
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("Masukan File dengan Format .pub")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

    def ReadSignKeyFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File")
        return (fname[0])

    def PopUpVerif(self):
        if (SignVerif.namefile == '' or SignVerif.pubfile == ''):
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("Masukan File ataupun Public Key File yang Masih Kosong")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            if (pathlib.Path(SignVerif.namefile).suffix == ".txt"):
                if (SignVerif.signfile != ''):
                    msg = QMessageBox()
                    msg.setWindowTitle("Notification")
                    msg.setText("Tidak Perlu Memasukkan Signed File untuk File .txt!")
                    msg.setIcon(QMessageBox.Question)
                    x = msg.exec_()
                else: 
                    with open("%s.pub" % (pathlib.Path(SignVerif.pubfile).stem), "rb") as rp:
                        tmp = rp.read()
                        key = str(tmp, 'utf-8').split(',')
                        d = int(key[1])
                        n = int(key[0])

                    with open("%s.txt" % (pathlib.Path(SignVerif.namefile).stem), "r+") as f:                
                        tmp = (f.read())
                        tmp2 = str(tmp, 'utf-8').split('\n<ds>')
                        print(tmp2)


                        tmp = dekripsi(hash(tmp), d, n)

                    with open('%s.txt' % (pathlib.Path(DigitalSign.namefile).stem), "a") as file:
                        file.write("\n<ds>")
                        file.write(tmp)
                        file.write("</ds>")
                        file.close()

                    msg = QMessageBox()
                    msg.setWindowTitle("Notification")
                    msg.setText("File Berhasil Di-sign")
                    msg.setIcon(QMessageBox.Information)
                    x = msg.exec_()
            else:
                print('x')
        # Warning
        # Critical
        # Information
        # Question

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
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QMainWindow, QMessageBox
from RSA import *
import os
import sys

def writeKey(fileName):
    p = generatePrima()
    q = generatePrima()
    n = p * q
    totient = (p - 1) * (q - 1)
    while True:
        e = generatePrima()
        if (totient % e != 0):
            break
    d = cariD(totient, e)
    
    if (os.path.exists("%s.pub" % (fileName)) or os.path.exists("%s.pri" % (fileName))):
        return False
    else:
        fo = open("%s.pri" % (fileName), "w")
        fo.write("%s,%s" % (n, e))
        fo.close()

        fo = open("%s.pub" % (fileName), "w")
        fo.write("%s,%s" % (n, d))
        fo.close()

        return True
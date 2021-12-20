#This program gets two values from a DB into lineEdits.
import sys
import os
from face_detect import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.sildetails)
     self.ui.pushButton_2.clicked.connect(self.analyse)
     self.ui.pushButton_3.clicked.connect(self.studetails)
     self.ui.pushButton_4.clicked.connect(self.adddetails)   
        

  def sildetails(self):
    os.system("python person1.py")

  def analyse(self):
    os.system("python identify1.py")

  def studetails(self):
    os.system("python studentdtls1.py")

  def adddetails(self):
    os.system("python adddtls1.py")

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

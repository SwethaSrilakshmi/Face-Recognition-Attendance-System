#This program gets two values from a DB into lineEdits.
import sys
import os
from person import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('frdb1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)

  def insertvalues(self):
         
     with con:
       cur = con.cursor()
       s4 = str(self.ui.lineEdit_4.text()) 
       s5 = str(self.ui.lineEdit_5.text()) 
        #picdata = open(s5, 'rb').read()
	#s6 = str(self.ui.lineEdit_6.text())
	#s7 = str(self.ui.lineEdit_7.text()) 
       cur.execute('INSERT INTO stuphoto VALUES(?,?)',(s4,s5)) 
       con.commit()

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

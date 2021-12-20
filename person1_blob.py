#This program gets two values from a DB into lineEdits.
import sys
import os
from person import *

import MySQLdb as mdb

con = mdb.connect('localhost', 'team1', 'test623', 'frdb1'); 

class MyForm(QtGui.QMainWindow):
  def __init__(self,parent=None):
     QtGui.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.insertvalues)
     #QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.imagedetails)

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        s4 = str(self.ui.lineEdit_4.text()) 
	s5 = str(self.ui.lineEdit_5.text()) 
        #picdata = open(s5, 'rb').read()
	#s6 = str(self.ui.lineEdit_6.text())
	#s7 = str(self.ui.lineEdit_7.text()) 
	cur.execute('INSERT INTO students VALUES(%s,%s)',(s4,picdata)) 
 	con.commit()

#  def imagedetails(self):
#    os.system("python disease1.py")     

if __name__ == "__main__":  
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

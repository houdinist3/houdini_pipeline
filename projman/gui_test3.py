from PySide2 import QtWidgets,QtCore
#from PyQt5 import QtWidgets,QtCore
import sys


#from hutil.Qt import QtWidgets, QtCore

class BScalender(QtWidgets.QWidget):
    def __init__(self):
        super(BScalender,self).__init__()
        # self.onCreateInterface()
        #print 'creating calender'
        #creat widget
        self.calender = QtWidgets.QCalendarWidget()
        self.title = QtWidgets.QLabel('TO Calender!')
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setStyleSheet('color:green; font-size:20px;')


        #layout
        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.calender)

        self.setLayout(layout)



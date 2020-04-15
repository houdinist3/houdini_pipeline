import hou
import os
import sys
# from hutil.Qt import QtWidgets
from PySide2 import QtWidgets, QtUiTools, QtCore

print 'hello TO'

class projectManager(QtWidgets.QWidget):
    def __init__(self):
        super(projectManager, self).__init__()
        self.proj = hou.getenv('JOB') + '/'

        #load UI file
        loder = QtUiTools.QUiLoader()
        self.ui = loder.load('/Users/byungsoo/houdini_env/Work/_houdini_/scripts/projman/projman.ui')

        #get ui elements
        self.setproj = self.ui.findChild(QtWidgets.QPushButton, 'setproj')
        self.projpath = self.ui.findChild(QtWidgets.QLabel, 'projpath')
        self.projname = self.ui.findChild(QtWidgets.QLabel, 'projname')
        self.scenelist = self.ui.findChild(QtWidgets.QListWidget, 'scenelist')

        #create widgets
        # self.btn = QtWidgets.QPushButton('click me')
        # self.lblTitle = QtWidgets.QLabel('PROJECT TO')
        # self.label = QtWidgets.QLabel(self.proj)
        #
        # self.listwidget = QtWidgets.QListWidget()

        #create connections
        self.setproj.clicked.connect(self.setproject)



        #layout
        root_widget = QtWidgets.QWidget()
        mainLayout = QtWidgets.QVBoxLayout()

        mainLayout.addWidget(self.ui)


        #Add widgets to layout
        # mainLayout.addWidget(self.lblTitle)
        # #mainLayout.addWidget(self.label)
        # mainLayout.addWidget(self.listwidget)
        # mainLayout.addWidget(self.btn)


        self.setLayout(mainLayout)
        self.setLayout(mainLayout)

    def setproject(self):
        setjob = hou.ui.selectFile(title='set project', file_type=hou.fileType.Directory)
        hou.hscript('setenv JOB' + setjob)

        print setjob

        # self.proj = hou.getenv('JOB') + '/'
        self.proj = setjob

        projname = setjob.split('/')[-2]
        setjob = os.path.dirname(setjob)
        projpath = os.path.split(setjob)[0]

        self.projname.setText(projname)
        self.projpath.setText(projpath + '/')
        self.onCreateInterface()






    def openScene(self, item):
        print 'open hipnc file~!'
        hipfile = self.proj + item.data()
        # open hip file
        print hipfile
        hou.hipFile.load(hipfile)

    def onCreateInterface(self):
        print 'creating interface'
        self.scenelist.clear()

        for file in os.listdir(self.proj):
            if file.endswith('.hipnc'):
                self.scenelist.addItem(file)

        # connect list items to fuction
        self.scenelist.doubleClicked.connect(self.openScene)



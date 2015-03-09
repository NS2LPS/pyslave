# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScriptWindow.ui'
#
# Created: Mon Mar  9 09:28:31 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(601, 422)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_Pause = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Pause.setObjectName(_fromUtf8("pushButton_Pause"))
        self.horizontalLayout.addWidget(self.pushButton_Pause)
        self.pushButton_Resume = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Resume.setObjectName(_fromUtf8("pushButton_Resume"))
        self.horizontalLayout.addWidget(self.pushButton_Resume)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Abort = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Abort.setObjectName(_fromUtf8("pushButton_Abort"))
        self.horizontalLayout.addWidget(self.pushButton_Abort)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Slave", None))
        self.pushButton_Pause.setText(_translate("MainWindow", "Pause", None))
        self.pushButton_Resume.setText(_translate("MainWindow", "Resume", None))
        self.pushButton_Abort.setText(_translate("MainWindow", "Abort", None))


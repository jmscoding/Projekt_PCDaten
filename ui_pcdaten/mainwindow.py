# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pcdaten\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.addUser = QtWidgets.QPushButton(self.centralwidget)
        self.addUser.setObjectName("addUser")
        self.gridLayout.addWidget(self.addUser, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.addDevice = QtWidgets.QPushButton(self.centralwidget)
        self.addDevice.setObjectName("addDevice")
        self.gridLayout.addWidget(self.addDevice, 0, 0, 1, 1)
        self.searchDevice = QtWidgets.QPushButton(self.centralwidget)
        self.searchDevice.setObjectName("searchDevice")
        self.gridLayout.addWidget(self.searchDevice, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addUser.setText(_translate("MainWindow", "Benutzer hinzufügen"))
        self.pushButton_4.setText(_translate("MainWindow", "Benutzer suchen"))
        self.addDevice.setText(_translate("MainWindow", "Gerät hinzufügen"))
        self.searchDevice.setText(_translate("MainWindow", "Gerät suchen"))

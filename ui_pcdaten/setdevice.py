# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pcdaten\setdevice.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setDevice(object):
    def setupUi(self, setDevice):
        setDevice.setObjectName("setDevice")
        setDevice.resize(400, 300)
        self.label = QtWidgets.QLabel(setDevice)
        self.label.setGeometry(QtCore.QRect(20, 40, 351, 20))
        self.label.setObjectName("label")
        self.inputCsv = QtWidgets.QLineEdit(setDevice)
        self.inputCsv.setGeometry(QtCore.QRect(20, 80, 241, 22))
        self.inputCsv.setObjectName("inputCsv")
        self.searchCsv = QtWidgets.QPushButton(setDevice)
        self.searchCsv.setGeometry(QtCore.QRect(270, 80, 93, 28))
        self.searchCsv.setObjectName("searchCsv")

        self.retranslateUi(setDevice)
        QtCore.QMetaObject.connectSlotsByName(setDevice)

    def retranslateUi(self, setDevice):
        _translate = QtCore.QCoreApplication.translate
        setDevice.setWindowTitle(_translate("setDevice", "Form"))
        self.label.setText(_translate("setDevice", "Hinzufügen der CSV Datei:"))
        self.searchCsv.setText(_translate("setDevice", "Durchsuchen"))

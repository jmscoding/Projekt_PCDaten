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
        setDevice.resize(400, 94)
        self.gridLayout = QtWidgets.QGridLayout(setDevice)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(setDevice)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inputCsv = QtWidgets.QLineEdit(setDevice)
        self.inputCsv.setObjectName("inputCsv")
        self.gridLayout.addWidget(self.inputCsv, 1, 0, 1, 1)
        self.searchCsv = QtWidgets.QPushButton(setDevice)
        self.searchCsv.setObjectName("searchCsv")
        self.gridLayout.addWidget(self.searchCsv, 1, 1, 1, 1)

        self.retranslateUi(setDevice)
        QtCore.QMetaObject.connectSlotsByName(setDevice)

    def retranslateUi(self, setDevice):
        _translate = QtCore.QCoreApplication.translate
        setDevice.setWindowTitle(_translate("setDevice", "Form"))
        self.label.setText(_translate("setDevice", "Hinzufügen der CSV Datei:"))
        self.searchCsv.setText(_translate("setDevice", "Durchsuchen"))
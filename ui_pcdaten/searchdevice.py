# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pcdaten\searchdevice.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_searchDevice(object):
    def setupUi(self, searchDevice):
        searchDevice.setObjectName("searchDevice")
        searchDevice.resize(493, 304)
        self.gridLayout = QtWidgets.QGridLayout(searchDevice)
        self.gridLayout.setObjectName("gridLayout")
        self.lineSearchDevices = QtWidgets.QLineEdit(searchDevice)
        self.lineSearchDevices.setObjectName("lineSearchDevices")
        self.gridLayout.addWidget(self.lineSearchDevices, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(searchDevice)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.searchDevices = QtWidgets.QPushButton(searchDevice)
        self.searchDevices.setObjectName("searchDevices")
        self.gridLayout.addWidget(self.searchDevices, 1, 1, 1, 1)
        self.listDevices = QtWidgets.QListView(searchDevice)
        self.listDevices.setObjectName("listDevices")
        self.gridLayout.addWidget(self.listDevices, 2, 0, 1, 2)

        self.retranslateUi(searchDevice)
        QtCore.QMetaObject.connectSlotsByName(searchDevice)

    def retranslateUi(self, searchDevice):
        _translate = QtCore.QCoreApplication.translate
        searchDevice.setWindowTitle(_translate("searchDevice", "Form"))
        self.label.setText(_translate("searchDevice", "Geben Sie Gerätenamen/ IP/ MAC/ Benutzer ein:"))
        self.searchDevices.setText(_translate("searchDevice", "Suchen"))

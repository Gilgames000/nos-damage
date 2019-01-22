# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/select_defenders.ui',
# licensing of 'gui/select_defenders.ui' applies.
#
# Created: Mon Jan 21 23:12:40 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SelectDefenders(object):
    def setupUi(self, SelectDefenders):
        SelectDefenders.setObjectName("SelectDefenders")
        SelectDefenders.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(SelectDefenders)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(SelectDefenders)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem(self.listWidget)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item = QtWidgets.QListWidgetItem(self.listWidget)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        QtWidgets.QListWidgetItem(self.listWidget)
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.pushButton = QtWidgets.QPushButton(SelectDefenders)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(SelectDefenders)
        QtCore.QMetaObject.connectSlotsByName(SelectDefenders)

    def retranslateUi(self, SelectDefenders):
        SelectDefenders.setWindowTitle(QtWidgets.QApplication.translate("SelectDefenders", "Dialog", None, -1))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtWidgets.QApplication.translate("SelectDefenders", "a", None, -1))
        self.listWidget.item(1).setText(QtWidgets.QApplication.translate("SelectDefenders", "b", None, -1))
        self.listWidget.item(2).setText(QtWidgets.QApplication.translate("SelectDefenders", "c", None, -1))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(QtWidgets.QApplication.translate("SelectDefenders", "PushButton", None, -1))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../秒杀.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class KillerUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(500, 520)
        MainWindow.setMinimumSize(QtCore.QSize(500, 520))
        MainWindow.setMaximumSize(QtCore.QSize(500, 520))
        MainWindow.setAcceptDrops(True)
        self.SameProductList = QtWidgets.QListWidget(MainWindow)
        self.SameProductList.setGeometry(QtCore.QRect(0, 0, 200, 300))
        self.SameProductList.setMinimumSize(QtCore.QSize(200, 300))
        self.SameProductList.setMaximumSize(QtCore.QSize(200, 300))
        self.SameProductList.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.SameProductList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SameProductList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.SameProductList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SameProductList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.SameProductList.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.SameProductList.setProperty("showDropIndicator", True)
        self.SameProductList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.SameProductList.setSelectionRectVisible(True)
        self.SameProductList.setObjectName("SameProductList")
        self.SameKillerList = QtWidgets.QListWidget(MainWindow)
        self.SameKillerList.setGeometry(QtCore.QRect(300, 0, 200, 300))
        self.SameKillerList.setMinimumSize(QtCore.QSize(200, 300))
        self.SameKillerList.setMaximumSize(QtCore.QSize(200, 300))
        self.SameKillerList.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.SameKillerList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SameKillerList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.SameKillerList.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.SameKillerList.setAlternatingRowColors(True)
        self.SameKillerList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.SameKillerList.setSelectionRectVisible(True)
        self.SameKillerList.setObjectName("SameKillerList")
        self.Add = QtWidgets.QPushButton(MainWindow)
        self.Add.setGeometry(QtCore.QRect(210, 80, 75, 30))
        self.Add.setObjectName("Add")
        self.Del = QtWidgets.QPushButton(MainWindow)
        self.Del.setGeometry(QtCore.QRect(210, 170, 75, 30))
        self.Del.setObjectName("Del")
        self.Console = QtWidgets.QTextBrowser(MainWindow)
        self.Console.setGeometry(QtCore.QRect(0, 320, 500, 200))
        self.Console.setMinimumSize(QtCore.QSize(500, 200))
        self.Console.setMaximumSize(QtCore.QSize(500, 200))
        self.Console.setObjectName("Console")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "秒杀"))
        self.Add.setText(_translate("MainWindow", "添加"))
        self.Del.setText(_translate("MainWindow", "取消"))


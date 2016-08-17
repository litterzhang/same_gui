# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workspace\SameKiller\登录.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class LoginUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(300, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 200))
        MainWindow.setMaximumSize(QtCore.QSize(300, 200))
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UserName = QtWidgets.QTextEdit(self.centralwidget)
        self.UserName.setGeometry(QtCore.QRect(90, 40, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.UserName.setFont(font)
        self.UserName.setFocusPolicy(QtCore.Qt.TabFocus)
        self.UserName.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.UserName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UserName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UserName.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.UserName.setTabChangesFocus(True)
        self.UserName.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.UserName.setAcceptRichText(False)
        self.UserName.setObjectName("UserName")
        self.Password = QtWidgets.QTextEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(90, 90, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.Password.setFont(font)
        self.Password.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Password.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Password.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Password.setTabChangesFocus(True)
        self.Password.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.Password.setAcceptRichText(False)
        self.Password.setObjectName("Password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 60, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 60, 30))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(110, 140, 80, 30))
        self.Login.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Login.setObjectName("Login")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.Login.setText(_translate("MainWindow", "登录"))
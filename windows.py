#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'窗口'

__author__ = 'litter_zhang'

import sys
from PyQt5 import QtWidgets
from login import login_win
from killer import killer_win

app = QtWidgets.QApplication(sys.argv)
login_show = login_win()
killer_show = killer_win()

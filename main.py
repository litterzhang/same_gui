#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same APP 黑子'

__author__ = 'litter_zhang'

import sys
from login import login_win
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
login_show = login_win()
login_show.show()
sys.exit(app.exec_())
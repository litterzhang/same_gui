#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same APP 黑子'

__author__ = 'litter_zhang'

import sys
from PyQt5 import QtWidgets
import utils.auth as AUTH
import utils.windows as WINDOWS
from killer import killer_win
from login import login_win

app = QtWidgets.QApplication(sys.argv)

if not AUTH.auth_login_with_token():
	WINDOWS._login_show = login_win()
	WINDOWS._login_show.show()
else:
	WINDOWS._killer_show = killer_win()
	WINDOWS._killer_show.show()

sys.exit(app.exec_())
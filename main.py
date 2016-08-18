#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same APP 黑子'

__author__ = 'litter_zhang'

import sys
import auth
import windows

if not auth.auth_login_with_token():
	windows.login_show.show()
else:
	windows.killer_show.show()

sys.exit(windows.app.exec_())
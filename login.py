#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same登录'

__author__ = 'litter_zhang'

from PyQt5 import QtWidgets
from UI.LoginUI import LoginUI
from settings import LOGIN_DATA, LOGIN_URL
from killer import killer_win
import utils.auth as AUTH
import utils.windows as WINDOWS

class login_win(QtWidgets.QMainWindow, LoginUI):
	def __init__(self):
		super(login_win, self).__init__()
		self.setupUi(self)

		self.Login.clicked.connect(self._login)

	def _login(self):
		username = self.UserName.text().strip()
		password = self.Password.text().strip()

		res_login, res_login_msg = same_login(username, password)

		if res_login:
			QtWidgets.QMessageBox.information(self, "成功", res_login_msg)
			self.close()

			WINDOWS._killer_show = killer_win()
			WINDOWS._killer_show.show()
		else:
			QtWidgets.QMessageBox.critical(self, "错误", res_login_msg)

def same_login(username, password):
	LOGIN_DATA['mobile'] = '+86-' + str(username)
	LOGIN_DATA['password'] = password

	r = AUTH._session.post(LOGIN_URL, data=LOGIN_DATA, auth=AUTH._auth)
	r.encoding = 'utf-8'
	try:
		r_j = r.json()
		code = r_j['code']
		if code==0:
			AUTH.auth_login(r_j['data']['user'])
		else:
			raise Exception(r_j['detail'])
	except Exception as e:
		return False, '登录失败：%s' % str(e)
	return True, '登录成功：%s' % AUTH._user['mobile']


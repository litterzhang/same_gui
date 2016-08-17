#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same登录'

__author__ = 'litter_zhang'

from PyQt5 import QtWidgets
from UI.LoginUI import LoginUI
from settings import LOGIN_DATA, LOGIN_URL
import auth as AUTH

class login_win(QtWidgets.QMainWindow, LoginUI):
	def __init__(self):
		super(login_win, self).__init__()
		self.setupUi(self)

		self.Login.clicked.connect(self._login)

	def _login(self):
		username = self.UserName.toPlainText()
		password = self.Password.toPlainText()

		res_login = same_login(username, password)
		print(res_login)

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
			raise r_j['detail']
	except Exception as e:
		return '登录失败：%s' % str(e)
	return '登录成功：%s' % AUTH._user['mobile']


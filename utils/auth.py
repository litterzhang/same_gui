#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same auth信息'

__author__ = 'litter_zhang'

import requests
import json
from utils.same import ImSameClient, LoginSameClient
from settings import AUTH_TOKEN_FILENAME

_session = requests.session()
_auth = ImSameClient()
_user = None

def auth_login(user):
	global _auth, _user
	_user = user
	_auth = LoginSameClient(_user['token'])

	# 写入token信息
	user_str = json.dumps(_user, ensure_ascii=False)
	with open(AUTH_TOKEN_FILENAME, 'w', encoding='utf-8') as fw:
		fw.write(user_str)

def auth_login_with_token():
	try:
		global _auth, _user
		user_str = ''
		with open(AUTH_TOKEN_FILENAME, 'r', encoding='utf-8') as fr:
			for line in fr:
				user_str += line.strip()
		user = json.loads(user_str)

		_user = user
		_auth = LoginSameClient(_user['token'])
	except Exception as e:
		# print(e)
		return False
	return True

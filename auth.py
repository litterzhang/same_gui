#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same auth信息'

__author__ = 'litter_zhang'

import requests
from utils.same import ImSameClient, LoginSameClient

_session = requests.session()
_auth = ImSameClient()
_user = None

def auth_login(user):
	global _auth, _user
	_user = user
	_auth = LoginSameClient(_user['token'])
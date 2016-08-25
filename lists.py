#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same 列表信息'

__author__ = 'litter_zhang'

_product_list = list()

_killer_list = list()

def change_product_list(_list):
	global _product_list
	_product_list = _list

def add_killer(_killer_thread):
	global _killer_list
	_killer_list.append(_killer_thread)
#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same登录'

__author__ = 'litter_zhang'

from PyQt5 import QtWidgets
from UI.KillerUI import KillerUI
from UI.ProductListItemUI import ProductListItemUI
from UI.KillerListItemUI import KillerListItemUI
from settings import SENSES_URL, ADDRESS_ID, KILLER_URL, TIME_URL
import utils.auth as AUTH
import utils.windows as WINDOWS
import threading
import time

class killer_win(QtWidgets.QMainWindow, KillerUI):
	def __init__(self):
		super(killer_win, self).__init__()
		self.setupUi(self)

		# 显示可秒杀的商品列表
		products = load_product_list()
		for product in products:
			p_item = ProductListItemUI(self.SameProductList)
			p_item.setProductData(product)

		self.Add.clicked.connect(self.start_killer)
		self.Del.clicked.connect(self.stop_killer)
		

	def stop_killer(self):
		for selected in self.SameKillerList.selectedItems():
			item = self.SameKillerList.itemWidget(selected)
			item.stopKiller()

	def start_killer(self):
		#获取选中商品
		for selected in self.SameProductList.selectedItems():
			selected.setSelected(False)

			item = self.SameProductList.itemWidget(selected)
			product = item.ProductData
			p_id = product.get('id', None)
			if p_id in WINDOWS._killer_list:
				self.Console.append('%s 已经在秒杀列表!' % p_id)
			else:
				WINDOWS._killer_list.append(p_id)
				# 显示到带秒杀列表中
				k_item = KillerListItemUI(self.SameKillerList, console=self.Console)
				k_item.setProductData(product)

#获取系统时间
def get_time():
	url = TIME_URL

	try:
		r = AUTH._session.get(url, auth=AUTH._auth)
		r.encoding = 'utf-8'

		time = r.json()['data']['time']

		return time/1000
	except Exception as e:
		# print(e)
		raise Exception('获取当前时间出错')

#加载商品列表
def load_product_list():
	url = SENSES_URL

	try:
		r = AUTH._session.get(url, auth=AUTH._auth)
		r.encoding = 'utf-8'

		products = [it['media']['product'] for it in r.json()['data']['results']]
		products = list(filter(lambda x: x['count_remaining'] is not 0, products))
		
		return products
	except Exception as e:
		# print(e)
		pass
